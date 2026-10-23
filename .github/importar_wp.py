# Copia todo lo publico de un sitio WordPress a la carpeta fuente/ (paginas, entradas, imagenes, documentos)
import json, os, re, urllib.request, urllib.parse, sys
SITIO = open('.github/sitio.txt').read().strip().rstrip('/')
HOST = urllib.parse.urlparse(SITIO).netloc.replace('www.', '')
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'}
os.makedirs('fuente/paginas', exist_ok=True); os.makedirs('fuente/medios', exist_ok=True)
log = []
def get(u, binario=False):
    r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60)
    d = r.read(); return d if binario else d.decode('utf-8', 'replace')
def guardar(p, d):
    os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
    open(p, 'wb' if isinstance(d, bytes) else 'w', **({} if isinstance(d, bytes) else {'encoding': 'utf-8'})).write(d)
def api(tipo):
    out, page = [], 1
    while True:
        try: j = json.loads(get(f'{SITIO}/wp-json/wp/v2/{tipo}?per_page=100&page={page}'))
        except Exception as e: log.append(f'API {tipo} p{page}: {e}'); break
        if not isinstance(j, list) or not j: break
        out += j; page += 1
        if len(j) < 100: break
    guardar(f'fuente/{tipo}.json', json.dumps(out, ensure_ascii=False, indent=1)); return out
paginas = api('pages'); entradas = api('posts'); medios = api('media'); api('categories')
try: guardar('fuente/menus.json', get(f'{SITIO}/wp-json/wp/v2/menu-items?per_page=100'))
except Exception as e: log.append(f'menu-items: {e}')
htmls = {}
def bajar_html(u, nombre):
    try: h = get(u); guardar(f'fuente/paginas/{nombre}.html', h); htmls[nombre] = h
    except Exception as e: log.append(f'HTML {u}: {e}')
bajar_html(SITIO + '/', 'inicio')
for x in paginas + entradas: bajar_html(x['link'], x['slug'])
# todo archivo del propio sitio enlazado o usado: imagenes (con srcset) y documentos
urls = set(m.get('source_url') for m in medios if m.get('source_url'))
texto = '\n'.join(htmls.values()) + json.dumps(paginas + entradas)
texto = texto.replace('\\/', '/')
for u in re.findall(r'https?://[^\s"\'<>()]+', texto):
    u = u.rstrip('.,;')
    host = urllib.parse.urlparse(u).netloc.replace('www.', '')
    if host != HOST: continue
    if '/wp-content/uploads/' in u or re.search(r'\.(pdf|docx?|xlsx?|pptx?|zip|mp4|mp3)$', u, re.I):
        urls.add(u.split('?')[0])
lista = []
for u in sorted(urls):
    ruta = urllib.parse.unquote(urllib.parse.urlparse(u).path).lstrip('/')
    ruta = ruta.split('wp-content/uploads/', 1)[-1]
    dest = 'fuente/medios/' + ruta
    try:
        if not os.path.exists(dest): guardar(dest, get(u, True))
        lista.append({'url': u, 'archivo': dest})
    except Exception as e: log.append(f'ARCHIVO {u}: {e}')
guardar('fuente/medios.json', json.dumps(lista, ensure_ascii=False, indent=1))
guardar('fuente/registro.txt', '\n'.join(log) or 'Sin errores')
print(f'{len(htmls)} paginas, {len(lista)} archivos, {len(log)} errores'); print('\n'.join(log[:50]))
