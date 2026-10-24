# Generador de las páginas web de las empresas de Ricardo Londoño (modelo POLIANDES).
# Uso (desde la raíz del repositorio):  python3 generador/build.py
# Lee generador/sitio.py (contenido propio de cada web) y fuente/medios (imágenes copiadas de WordPress)
# y escribe las páginas en la raíz. El contenido editable (noticias, eventos, videos, fotos) vive en
# datos/contenido.json y se cambia desde el panel /admin; este generador NO lo pisa si ya existe.
import os, re, json, shutil, sys, html, importlib.util
from datetime import date

GEN = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(GEN)
FUENTE = os.path.join(os.path.dirname(GEN), 'fuente')
spec = importlib.util.spec_from_file_location('sitio', os.path.join(GEN, 'sitio.py'))
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
SITIO = S.SITIO
e = lambda s: html.escape(str(s or ''), quote=True)
ANIO = date.today().year

def leer(n): return open(os.path.join(GEN, n), encoding='utf-8').read()
def escribir(ruta, txt):
    p = os.path.join(RAIZ, ruta); os.makedirs(os.path.dirname(p) or RAIZ, exist_ok=True)
    open(p, 'w', encoding='utf-8').write(txt)

# ---------- imágenes: se copian de fuente/medios a img/ con nombres claros ----------
def copiar_imagenes():
    os.makedirs(os.path.join(RAIZ, 'img'), exist_ok=True)
    for dest, orig in SITIO['imagenes'].items():
        o = os.path.join(FUENTE, 'medios', orig)
        d = os.path.join(RAIZ, 'img', dest)
        if not os.path.exists(o): print('FALTA imagen', orig); continue
        try:
            from PIL import Image
            im = Image.open(o)
            if dest.endswith('.png'):
                im.thumbnail((900, 900)); im.save(d, optimize=True)
            else:
                im = im.convert('RGB'); im.thumbnail((1600, 1600)); im.save(d, 'JPEG', quality=82, optimize=True, progressive=True)
        except ImportError:
            shutil.copyfile(o, d)

# ---------- partes comunes ----------
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.4.5-.3.4c-.1.1-.3.3-.1.6.1.3.6 1.1 1.4 1.8 1 .9 1.8 1.1 2.1 1.3.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.4.2.5.3.1.2.1.7-.1 1.3z"/></svg>'
SKYNET_SVG = '<svg viewBox="0 0 200 200" aria-hidden="true"><rect x="4" y="4" width="192" height="192" rx="46" fill="#1E3A4C"/><g stroke="#FFFFFF" stroke-linecap="round"><polygon points="100,42 150.2,71 150.2,129 100,158 49.8,129 49.8,71" fill="none" stroke-opacity=".35" stroke-width="4"/><path d="M100 100L100 42M100 100L150.2 71M100 100L150.2 129M100 100L100 158M100 100L49.8 129M100 100L49.8 71" stroke-width="6"/></g><g fill="#FFFFFF"><circle cx="150.2" cy="71" r="10"/><circle cx="150.2" cy="129" r="10"/><circle cx="100" cy="158" r="10"/><circle cx="49.8" cy="129" r="10"/><circle cx="49.8" cy="71" r="10"/></g><circle cx="100" cy="42" r="13" fill="#E0A21A"/><circle cx="100" cy="100" r="20" fill="#E0A21A"/></svg>'

def enlace(it, clase=''):
    texto, href = it[0], it[1]
    extra = it[2] if len(it) > 2 else ''
    externo = href.startswith('http') and SITIO['dominio'] not in href.split('/')[2] if href.startswith('http') else False
    tgt = ' target="_blank" rel="noopener"' if externo else ''
    small = f'<small>{e(extra)}</small>' if extra else ''
    inner = f'<b>{e(texto)}</b>{small}' if extra else e(texto)
    return f'<a{" class=" + chr(34) + clase + chr(34) if clase else ""} href="{e(href)}"{tgt}>{inner}</a>'

def menu(activo):
    partes = []
    for m in SITIO['menu']:
        if isinstance(m[1], list):
            der = ' der' if m[0] == SITIO.get('menu_derecha') else ''
            cls = ' class="cta"' if m[0] == SITIO.get('menu_derecha') else ''
            partes.append(f'<div class="dd{der}"><button{cls}>{e(m[0])} ▾</button><div class="sub">' + ''.join(enlace(x) for x in m[1]) + '</div></div>')
        else:
            partes.append(enlace(m, 'activo' if m[1] == activo else ''))
    return '\n'.join(partes)

def cabecera(titulo, descripcion, activo):
    c = SITIO
    marca_img = f'<img src="/img/{c["logo"]}" alt="{e(c["nombre"])}">' if c.get('logo') else ''
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title><meta name="description" content="{e(descripcion)}">
<link rel="icon" href="/img/{c["icono"]}">
<meta property="og:title" content="{e(titulo)}"><meta property="og:description" content="{e(descripcion)}"><meta property="og:image" content="https://{c["dominio"]}/img/{c["og"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/estilos.css"></head><body>
<div class="aviso-top">{c["aviso_top"]}</div>
<header class="top"><div class="wrap">
<a class="marca" href="/">{marca_img}<div>{c["marca_html"]}<small>{e(c["lema_corto"])}</small></div></a>
<button class="hamb" aria-label="Abrir menú" onclick="document.getElementById('menu').classList.toggle('abierto')">☰</button>
<nav class="menu" id="menu">
{menu(activo)}
</nav>
</div></header>
'''

def pie():
    c = SITIO
    cols = ''.join(f'<div><h4>{e(t)}</h4>{h}</div>' for t, h in c['pie'])
    return f'''<footer><div class="wrap"><div class="cols">{cols}</div>
<div class="cred">{SKYNET_SVG} Sitio desarrollado por SkyNet Genesis · contacto@skynetgenesis.com · WhatsApp 304 437 5758 · © {ANIO} {e(c["nombre_corto"])} · <a class="ingresar" href="/admin/" rel="nofollow">Ingresar (equipo)</a> · <a class="ingresar" href="https://agenda-ia.skynetgenesis.com/" target="_blank" rel="nofollow noopener">Agenda-IA (funcionarios)</a></div>
</div></footer>
<script src="/docs.js" defer></script>
<a class="wa-flot" href="https://wa.me/{c["whatsapp"]}" aria-label="Escribir por WhatsApp">{WA_SVG}</a>
</body></html>
'''

def pagina(ruta, titulo, descripcion, cuerpo, activo=''):
    escribir(ruta, cabecera(titulo, descripcion, activo) + cuerpo + pie())

# ---------- 404 con redirecciones de direcciones viejas ----------
def pagina_404():
    mapa = json.dumps(SITIO['redirecciones'], ensure_ascii=False)
    raiz = json.dumps(SITIO['carpetas_en_siteground'])
    cuerpo = f'''<section><div class="wrap" style="text-align:center;padding:40px 16px">
<h1>Página no encontrada</h1><p class="sub-t" style="margin:0 auto 20px">La dirección que buscó cambió o ya no existe. Lo estamos llevando a la página correcta…</p>
<div class="btns" style="justify-content:center"><a class="btn b-az" href="/">Ir al inicio</a></div></div></section>
<script>(function(){{var M={mapa},R={raiz},p=location.pathname.replace(/\\/+$/,"/");
var s=p.split("/")[1]||"";if(R.indexOf(s)>=0){{location.replace("https://{SITIO["dominio_raiz"]}"+location.pathname+location.search+location.hash);return}}
var d=M[p]||M[p.replace(/\\/$/,"")];if(d)location.replace(d)}})();</script>
'''
    pagina('404.html', 'Página no encontrada · ' + SITIO['nombre_corto'], 'Página no encontrada', cuerpo)

# ---------- panel /admin (copiado del de POLIANDES, con la configuración de esta web) ----------
def panel():
    p = leer('panel.html')
    c = SITIO
    rep = [("'poliandes-web'", f"'{c['repo']}'"), ("'www.poliandes.com'", f"'{c['dominio']}'"),
           ('>www.poliandes.com<', f'>{c["dominio"]}<'), ("'panel-poliandes-llave'", f"'panel-{c['repo']}-llave'"),
           ('Panel de administración | POLIANDES', 'Panel de administración | ' + c['nombre_corto']),
           ('<i>Panel POLIANDES</i>', f'<i>Panel {c["nombre_corto"]}</i>'), ('<b>poliandes-web</b>', f'<b>{c["repo"]}</b>'),
           ('Noticias · HOY en POLIANDES', 'Noticias · ' + c['nombre_noticias']), ('«HOY en POLIANDES»', '«' + c['nombre_noticias'] + '»'),
           ('Fotos · Vida en POLIANDES', 'Fotos · ' + c['nombre_galeria']), ("'Poliandes Santa Marta 2026'", f"'{c['ejemplo_clave']}'")]
    for a, b in rep:
        if a not in p: print('AVISO panel: no encontré', a)
        p = p.replace(a, b)
    carp = ', '.join(f"{k}: '{v}'" for k, v in c['carpetas_documentos'].items())
    p, n = re.subn(r'carpetas: \{[^}]*\}', 'carpetas: {\n    ' + carp + '\n  }', p, count=1)
    if not n: print('AVISO panel: no encontré carpetas')
    if 'oliandes' in p.replace('poliandes.com/campus', ''): print('AVISO panel: quedó texto de POLIANDES:', set(re.findall(r'.{30}oliandes.{30}', p)))
    import ingreso_central; p = ingreso_central.convertir(p, c)  # servicio central de ingreso (directiva webs)
    escribir('admin/index.html', p)
    escribir('admin/acceso.js', leer('acceso.js'))
    if not os.path.exists(os.path.join(RAIZ, 'admin/accesos.json')): escribir('admin/accesos.json', '{"usuarios":[]}\n')
    escribir('robots.txt', f'User-agent: *\nDisallow: /admin/\nSitemap: https://{c["dominio"]}/sitemap.xml\n')

def scripts():
    d = leer('docs.js').replace('RL-rikardolondono/poliandes-web', 'RL-rikardolondono/' + SITIO['repo'])
    d = d.replace('© 2026 POLIANDES', '© ' + str(ANIO) + ' ' + SITIO['nombre_corto'])
    escribir('docs.js', d)
    escribir('contenido.js', leer('contenido.js').replace('/noticias.html#n-', '/noticias/#n-'))
    css = leer('base.css')
    css = re.sub(r':root\{[^}]*\}', ':root{' + SITIO['colores'] + '}', css, count=1) + '\n' + leer('extra.css') + '\n' + SITIO.get('css', '')
    escribir('estilos.css', css)
    # carpetas de documentos que el panel llena
    for k in SITIO['carpetas_documentos']:
        f = os.path.join(RAIZ, 'documentos', k, 'LEEME.md')
        if not os.path.exists(f): escribir(f'documentos/{k}/LEEME.md', f'# {SITIO["carpetas_documentos"][k]}\n\nLos documentos de esta carpeta se suben desde el panel /admin (pestaña Documentos).\n')

def contenido_inicial():
    f = os.path.join(RAIZ, 'datos/contenido.json')
    if os.path.exists(f): return
    escribir('datos/contenido.json', json.dumps(SITIO['contenido_inicial'], ensure_ascii=False, indent=1))

def sitemap(rutas):
    urls = ''.join(f'<url><loc>https://{SITIO["dominio"]}/{r}</loc></url>' for r in rutas)
    escribir('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')

def main():
    copiar_imagenes(); scripts(); panel(); contenido_inicial()
    rutas = []
    for p in S.PAGINAS:
        pagina(p['ruta'], p['titulo'], p['descripcion'], p['cuerpo'], p.get('activo', ''))
        rutas.append(p['ruta'].replace('index.html', ''))
    pagina_404(); sitemap(rutas)
    escribir('CNAME', SITIO['dominio'] + '\n')
    escribir('.nojekyll', '')
    print('Listo:', len(S.PAGINAS), 'páginas en', RAIZ)

if __name__ == '__main__': main()
