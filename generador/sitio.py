# Contenido de www.reinaelizabeth.com (Reina Elizabeth IPS). Lo usa generador/build.py.
WA = '573128886611'
RAIZ = 'https://reinaelizabeth.com'   # se queda en SiteGround solo para las herramientas (tests, OsTicket, ContaIPS…)

def ic(d):
    return f'<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I = {
    'medico': ic('<path d="M6 3v6a6 6 0 0 0 12 0V3"/><path d="M12 15v3a3 3 0 0 0 6 0v-1"/><circle cx="18" cy="15" r="2"/>'),
    'casa': ic('<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M12 13v5M9.5 15.5h5"/>'),
    'proc': ic('<rect x="3" y="7" width="18" height="12" rx="2"/><path d="M9 7V5h6v2M12 10v6M9 13h6"/>'),
    'cura': ic('<path d="M10.5 3.5l10 10-7 7-10-10z"/><path d="M8 8l8 8"/><circle cx="12" cy="12" r=".6"/>'),
    'enf': ic('<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z"/>'),
    'vac': ic('<path d="M18 2l4 4M15 5l4 4M6 13l5 5M4 20l3-3M8 9l7 7-4 4-7-7z"/><path d="M14 4l6 6"/>'),
    'psi': ic('<path d="M12 3a7 7 0 0 0-7 7c0 2.5 1.3 4 3 5v6h6v-3h2a2 2 0 0 0 2-2v-3l2-1-2-3a7 7 0 0 0-6-6z"/>'),
    'cerebro': ic('<path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0-2 5 3 3 0 0 0 3 4 3 3 0 0 0 5 1V5a2 2 0 0 0-3-1zM15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 2 5 3 3 0 0 1-3 4 3 3 0 0 1-5 1"/>'),
    'terapia': ic('<circle cx="12" cy="4.5" r="2"/><path d="M12 7v7M8 10h8M9 21l3-7 3 7"/>'),
    'reloj': ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
}

SITIO = {
    'nombre': 'Reina Elizabeth IPS', 'nombre_corto': 'Reina Elizabeth IPS', 'repo': 'reina-elizabeth-web',
    'dominio': 'www.reinaelizabeth.com', 'dominio_raiz': 'reinaelizabeth.com', 'whatsapp': WA,
    'logo': 'logo.png', 'icono': 'logo.png', 'og': 'recepcion.jpg',
    'marca_html': 'REINA <span>ELIZABETH</span>', 'lema_corto': 'IPS · Santa Marta',
    'aviso_top': f'Urgencias médicas 24 horas · WhatsApp <a href="https://wa.me/{WA}">312 888 6611</a> · Calle 22 No. 18-18, Santa Marta',
    'nombre_noticias': 'Noticias de Reina Elizabeth', 'nombre_galeria': 'Nuestra IPS', 'ejemplo_clave': 'Reina Elizabeth 2026',
    'colores': '--azul:#0B4F8A;--azul-osc:#073560;--celeste:#14A38B;--naranja:#14A38B;--cta-txt:#fff;--oro-osc:#0E8571;--oro-suave:#E3F6F2;--verde:#1F8A4C;--fondo:#F4F8FB;--fondo2:#E8F1FA;--sup:#fff;--texto:#1C2B39;--suave:#5D6B78;--borde:#DCE5EE',
    'css': '.marca span{color:#7FE0CF}.marca img{width:auto;height:52px}.etq{color:#fff}.pill.n{color:#fff}.cifra{border-top-color:var(--celeste)}',
    'imagenes': {
        'logo.png': '2025/05/oso2re.png',
        'oso-grande.png': '2025/05/cropped-oso2re.png',
        'recepcion.jpg': '2025/05/Recepcion-IPS.jpeg',
        'vigilado-supersalud.png': '2025/05/logo-vigilado-supersalud.png',
        'supersalud.jpg': '2025/05/channels4_profile.jpg',
    },
    'carpetas_documentos': {
        'sgsst': 'SG-SST (Seguridad y Salud en el Trabajo)', 'institucional': 'Documentos institucionales',
        'formatos': 'Formatos para usuarios', 'academicos': 'Eventos académicos y docencia',
    },
    'carpetas_en_siteground': ['TDAH', 'atencionyvigiliatest', 'autiscan', 'conductas', 'contabilidad', 'contaips', 'cotizacion', 'ct-tdah',
        'formatosmedicos', 'growth', 'kessler-k10', 'mapasueno', 'memoria', 'osticketsoportealcliente', 'payroll-pro',
        'reina-elizabeth-ips-dosis', 'test-deficit-atencional.html', 'certificado-medico.html', 'sgsst-app.zip'],
    'redirecciones': {'/sample-page/': '/', '/author/adminre/': '/noticias/', '/category/sin-categoria/': '/noticias/', '/wp-admin/': '/admin/', '/wp-login.php': '/admin/'},
    'menu_derecha': 'Funcionarios',
    'menu': [
        ('Inicio', '/'),
        ('Servicios', [('Servicios de salud', '/#servicios'), ('Programa Autismo y Neurodivergencia', '/programa-autismo-y-neurodivergencia/'),
                       ('Intervención Temprana', '/intervencion-temprana/'), ('Regulación Sensorial', '/regulacion-sensorial/'),
                       ('Solicitar consulta', f'https://wa.me/{WA}?text=Hola%2C%20quiero%20solicitar%20una%20consulta')]),
        ('Educación y docencia', [('Eventos académicos', '/educacion/#eventos'), ('Test Atencional Básico', f'{RAIZ}/test-deficit-atencional.html'),
                                  ('Mapa de Sueño', f'{RAIZ}/mapasueno/mapasueno'), ('Test Atención y Vigilia', f'{RAIZ}/atencionyvigiliatest/atencionyvigiliatest'),
                                  ('Test de Memoria', f'{RAIZ}/memoria/memoria')]),
        ('Resultados de laboratorio', [('Mabel Otero', 'https://labmabelotero.com/'), ('Synlab', 'https://synlab.es/descargar-resultados'),
                                       ('Radiólogos Asociados', 'https://portalpaciente.rras-radioimagenes.com/Identity/Account/Login'),
                                       ('Imag', 'https://resultados.imagcentroradiologico.com:8443/PortalDicom/login')]),
        ('Noticias', '/noticias/'),
        ('Nuestra institución', [('Quiénes somos', '/institucion/'), ('SG-SST', '/institucion/#sgsst'), ('Trabaja con nosotros', '/institucion/#trabaja'),
                                 ('Soporte y asistencia (OsTicket)', f'{RAIZ}/osticketsoportealcliente/scp/login.php'), ('Contacto', '/#contacto')]),
        ('Funcionarios', [('Agenda-IA', 'https://agenda-ia.skynetgenesis.com/', 'Agenda de trabajo y tareas'), ('Biofile', 'https://reina.biofile.com.co/IniciarSesion.aspx?ReturnUrl=%2f'),
                          ('Control Integración', 'https://carteraintegracion.reinaelizabeth.com/'), ('Cotizaciones RE', f'{RAIZ}/cotizacion/cotizacion-reina-elizabeth.html'),
                          ('Certificado Médico Escolar', f'{RAIZ}/certificado-medico.html'), ('Formatos Médicos', f'{RAIZ}/formatosmedicos/'),
                          ('Evaluación Neuropsicología', f'{RAIZ}/conductas/evaluacion-infantil-cie11.html'), ('ContaIPS', f'{RAIZ}/contaips/'),
                          ('Sistema de Pagos', f'{RAIZ}/payroll-pro/payroll-pro-simple.html'), ('Tecnovigilancia', 'https://farmacoweb.invima.gov.co/TecnoVigilancia/faces/index.xhtml'),
                          ('Escala de Kessler 10', f'{RAIZ}/kessler-k10/'), ('AutiScan Analytics', f'{RAIZ}/autiscan/index.html'),
                          ('ChildGrowth', f'{RAIZ}/growth/childgrowth_html_v1.0/pacientes.html'), ('SISPRO', 'https://www.sispro.gov.co/Pages/Home.aspx'),
                          ('RIPS', 'https://www.sispro.gov.co/central-financiamiento/Pages/facturacion-electronica.aspx'),
                          ('Ver todas las herramientas', '/funcionarios/')]),
    ],
    'pie': [
        ('Reina Elizabeth IPS', 'Cuidamos tu salud con amor y fe.<br>MONTECARLO SHAIO CLÍNICA IPS S.A.S.<br>NIT 901074496<br><img class="logo-vig" src="/img/vigilado-supersalud.png" alt="Vigilado Supersalud" loading="lazy" style="margin-top:10px">'),
        ('Contacto', f'Calle 22 No. 18-18, Catalina 2000<br>Santa Marta, Magdalena<br>WhatsApp 24/7: <a href="https://wa.me/{WA}">312 888 6611</a><br>Correo: <a href="mailto:contacto@reinaelizabeth.com">contacto@reinaelizabeth.com</a>'),
        ('Servicios', '<ul><li><a href="/#servicios">Servicios de salud</a></li><li><a href="/programa-autismo-y-neurodivergencia/">Autismo y Neurodivergencia</a></li><li><a href="/intervencion-temprana/">Intervención Temprana</a></li><li><a href="/regulacion-sensorial/">Regulación Sensorial</a></li></ul>'),
        ('Enlaces', '<ul><li><a href="/noticias/">Noticias</a></li><li><a href="/educacion/">Educación y docencia</a></li><li><a href="/institucion/">Nuestra institución</a></li><li><a href="/funcionarios/">Funcionarios</a></li></ul>'),
    ],
    'contenido_inicial': {
        'noticias': [
            {'id': 'programa-autismo-y-neurodivergencia', 'fecha': '2025-05-08', 'titulo': 'Programa Autismo y Neurodivergencia', 'texto': 'Atención integral y personalizada para niños, niñas y adolescentes con condiciones del neurodesarrollo, especialmente Trastorno del Espectro Autista (TEA) y otras formas de neurodivergencia.', 'foto': '', 'enlace': '/programa-autismo-y-neurodivergencia/', 'textoEnlace': 'Ver el programa', 'video': ''},
            {'id': 'intervencion-temprana', 'fecha': '2025-05-08', 'titulo': 'Intervención Temprana', 'texto': 'Para niños y niñas entre los 0 y 5 años con variaciones en su desarrollo o condiciones neurológicas detectadas en etapas iniciales.', 'foto': '', 'enlace': '/intervencion-temprana/', 'textoEnlace': 'Ver el programa', 'video': ''},
            {'id': 'regulacion-sensorial', 'fecha': '2025-05-08', 'titulo': 'Regulación Sensorial', 'texto': 'Programa de Regulación Sensorial e Integración Neuromotora para niños y niñas con dificultades en el procesamiento de estímulos sensoriales.', 'foto': '', 'enlace': '/regulacion-sensorial/', 'textoEnlace': 'Ver el programa', 'video': ''},
        ],
        'eventos': [], 'videos': [],
        'galeria': [{'foto': '/img/recepcion.jpg', 'texto': 'Recepción de Reina Elizabeth IPS'}],
    },
}

# ---------------- contenido de las páginas ----------------
SERVICIOS = [
    ('medico', 'Medicina general', 'Consulta médica en la IPS y a domicilio.'),
    ('reloj', 'Urgencias médicas 24 horas', 'Atención de urgencias todos los días, a toda hora.'),
    ('casa', 'Enfermería a domicilio', 'Cuidados de enfermería en la comodidad de su casa.'),
    ('proc', 'Sala de procedimientos básicos', 'Procedimientos menores con personal capacitado.'),
    ('cura', 'Curaciones', 'Curación y seguimiento de heridas.'),
    ('vac', 'Vacunación especializada', 'Esquemas de vacunación con asesoría profesional.'),
    ('psi', 'Psicología', 'Valoración y acompañamiento psicológico.'),
    ('cerebro', 'Autismo y neurodivergencia', 'Evaluación e intervención interdisciplinaria (Autism Center).'),
    ('terapia', 'Terapias', 'Física, ocupacional, conductual y sensorial.'),
]
PROGRAMAS = [
    ('programa-autismo-y-neurodivergencia', 'Programa Autismo y Neurodivergencia', 'cerebro',
     'El programa de Autismo y Neurodivergencia de la IPS Reina Elizabeth está diseñado para brindar atención integral y personalizada a niños, niñas y adolescentes que presentan condiciones del neurodesarrollo, especialmente Trastorno del Espectro Autista (TEA) y otras formas de neurodivergencia. Este programa se fundamenta en un enfoque interdisciplinario que combina evaluación clínica especializada, intervención terapéutica individualizada y acompañamiento familiar, con el fin de promover la comunicación, la autonomía, la regulación emocional y la inclusión educativa y social.\n\nA través de modelos de intervención basados en evidencia, como TEACCH y otras metodologías estructuradas, garantizamos un entorno terapéutico respetuoso con los ritmos y necesidades de cada niño, asegurando un plan de atención integral (PIAR) ajustado a su perfil neuropsicológico y educativo.'),
    ('intervencion-temprana', 'Intervención Temprana', 'terapia',
     'El programa de Intervención Temprana en el Desarrollo Infantil de la IPS Reina Elizabeth está dirigido a niños y niñas entre los 0 y 5 años que presentan variaciones en su desarrollo o condiciones neurológicas detectadas en etapas iniciales.\n\nMediante un enfoque interdisciplinario que integra neuropsicología, fisioterapia, fonoaudiología, terapia ocupacional y acompañamiento familiar, este programa tiene como propósito fortalecer las áreas motora, comunicativa, cognitiva y socioemocional, aprovechando las ventanas de plasticidad cerebral propias de la primera infancia. La intervención se diseña de manera personalizada, respetando el perfil neurodesarrollativo de cada niño, para favorecer su autonomía, su participación activa en los entornos cotidianos y su bienestar integral.'),
    ('regulacion-sensorial', 'Regulación Sensorial', 'enf',
     'El programa de Regulación Sensorial e Integración Neuromotora de la IPS Reina Elizabeth está dirigido a niños y niñas que presentan dificultades en el procesamiento de estímulos sensoriales o alteraciones en la organización neuromotora que afectan su participación en actividades cotidianas.\n\nMediante un enfoque terapéutico especializado que combina terapia ocupacional, fisioterapia y estimulación multisensorial, el programa busca favorecer la autorregulación, el control postural, la coordinación y la adaptación funcional en contextos familiares, escolares y sociales. Cada intervención se diseña de forma individualizada, considerando el perfil sensorial y motor del niño, dentro de un ambiente estructurado que promueve la exploración segura, la autonomía y el bienestar integral.'),
]
RES = {'programa-autismo-y-neurodivergencia': 'Atención integral para niños, niñas y adolescentes con TEA y otras formas de neurodivergencia.', 'intervencion-temprana': 'Para niños de 0 a 5 años con variaciones en su desarrollo o condiciones neurológicas.', 'regulacion-sensorial': 'Regulación sensorial e integración neuromotora para la vida cotidiana.'}
WA_CONSULTA = f'https://wa.me/{WA}?text=Hola%2C%20quiero%20solicitar%20una%20consulta'

def servicios_html():
    return '<div class="servicios">' + ''.join(f'<div class="servicio"><span class="ico">{I[i]}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in SERVICIOS) + '</div>'

def programas_html():
    return '<div class="servicios">' + ''.join(
        f'<a class="servicio" href="/{s}/" style="text-decoration:none;color:inherit"><span class="ico">{I[i]}</span><h3>{t}</h3><p>{RES[s]}</p><span class="mas">Conocer el programa →</span></a>'
        for s, t, i, txt in PROGRAMAS) + '</div>'

INICIO = f'''<div class="hero foto"><img class="fondo" src="/img/recepcion.jpg" alt=""><div class="wrap">
<span class="etq">Santa Marta · Autism Center</span><h1>Reina Elizabeth IPS</h1>
<p>Cuidamos tu salud con amor y fe. Medicina general en la IPS y a domicilio, urgencias médicas las 24 horas, enfermería, vacunación, psicología y un programa especializado en autismo y neurodivergencia.</p>
<div class="btns"><a class="btn b-wa" href="{WA_CONSULTA}">Solicitar consulta por WhatsApp</a><a class="btn b-bl" href="/programa-autismo-y-neurodivergencia/">Programa de autismo</a></div></div></div>
<div class="wrap"><div class="cifras">
<div class="cifra"><b>24/7</b><span>Urgencias médicas todos los días</span></div>
<div class="cifra"><b>A domicilio</b><span>Medicina general y enfermería en su casa</span></div>
<div class="cifra"><b>Autism Center</b><span>Autismo y neurodivergencia con enfoque interdisciplinario</span></div>
<div class="cifra"><b>Santa Marta</b><span>Calle 22 No. 18-18, Catalina 2000</span></div>
</div></div>
<section id="servicios"><div class="wrap"><h2>Servicios de salud</h2><p class="sub-t">Atención humana y profesional para toda la familia.</p>{servicios_html()}</div></section>
<section class="alt"><div class="wrap"><h2>Programas especializados</h2><p class="sub-t">Atención interdisciplinaria para niños, niñas y adolescentes.</p>{programas_html()}</div></section>
<section><div class="wrap"><div class="dos"><div><h2>Noticias</h2><div class="grid" data-bloque="noticias-inicio"></div>
<p style="margin-top:14px"><a class="mas" href="/noticias/">Ver todas las noticias →</a></p></div>
<aside><div class="box"><h2 style="font-size:1.4rem">Eventos académicos</h2><div data-bloque="eventos"><p style="color:var(--suave)">Pronto anunciaremos nuevos eventos.</p></div></div></aside></div></div></section>
<section class="alt"><div class="wrap"><div class="foto-texto"><img src="/img/recepcion.jpg" alt="Recepción de Reina Elizabeth IPS" loading="lazy">
<div><h2>Nuestra IPS</h2><p>Estamos en Santa Marta, en la Calle 22 No. 18-18. Contamos con recepción, consultorios, sala de procedimientos, farmacia y sala de espera, con un equipo comprometido con la atención humanizada.</p>
<p><b>Visión al 2030:</b> ser un centro de excelencia en servicios de salud de alta complejidad.</p>
<div class="btns"><a class="btn b-az" href="/institucion/">Conocer la institución</a></div></div></div></div></section>
<section><div class="wrap"><h2>Galería</h2><div class="galeria" data-bloque="galeria"></div></div></section>
<section class="alt" id="resultados"><div class="wrap"><h2>Resultados de laboratorio e imágenes</h2><p class="sub-t">Consulte sus resultados directamente en el portal de cada laboratorio.</p><div class="accesos">
<a class="acceso" href="https://labmabelotero.com/" target="_blank" rel="noopener"><span class="ico">LAB</span><span><b>Mabel Otero</b><small>Laboratorio clínico</small></span></a>
<a class="acceso" href="https://synlab.es/descargar-resultados" target="_blank" rel="noopener"><span class="ico">LAB</span><span><b>Synlab</b><small>Descargar resultados</small></span></a>
<a class="acceso" href="https://portalpaciente.rras-radioimagenes.com/Identity/Account/Login" target="_blank" rel="noopener"><span class="ico">RX</span><span><b>Radiólogos Asociados</b><small>Portal del paciente</small></span></a>
<a class="acceso" href="https://resultados.imagcentroradiologico.com:8443/PortalDicom/login" target="_blank" rel="noopener"><span class="ico">RX</span><span><b>Imag</b><small>Centro radiológico</small></span></a>
</div></div></section>
<div class="franja"><div class="wrap"><div><h2>¿Necesita atención?</h2><p>Escríbanos por WhatsApp las 24 horas, todos los días.</p></div><a class="btn b-wa" href="{WA_CONSULTA}">WhatsApp 312 888 6611</a></div></div>
<section id="contacto"><div class="wrap"><h2>Contacto</h2><div class="contacto-grid">
<div class="box"><h3>Dirección</h3><p style="margin:0">Calle 22 No. 18-18, Catalina 2000<br>Santa Marta, Magdalena</p><p style="margin:8px 0 0"><a class="mas" href="https://www.google.com/maps/search/?api=1&query=Calle+22+18-18+Santa+Marta" target="_blank" rel="noopener">Ver en el mapa →</a></p></div>
<div class="box"><h3>WhatsApp 24/7</h3><p style="margin:0"><a href="https://wa.me/{WA}">312 888 6611</a><br>Urgencias médicas las 24 horas</p></div>
<div class="box"><h3>Correo</h3><p style="margin:0"><a href="mailto:contacto@reinaelizabeth.com">contacto@reinaelizabeth.com</a></p></div>
</div></div></section>
'''

def programa(slug, titulo, icono, texto):
    parrafos = ''.join(f'<p>{p}</p>' for p in texto.split('\n\n'))
    return {'ruta': f'{slug}/index.html', 'titulo': f'{titulo} · Reina Elizabeth IPS', 'descripcion': texto.split('.')[0][:155], 'cuerpo': f'''
<div class="hero"><div class="wrap"><span class="etq">Programa especializado</span><h1>{titulo}</h1></div></div>
<section><div class="wrap"><div class="migas"><a href="/">Inicio</a> › <a href="/#servicios">Servicios</a> › {titulo}</div><div class="articulo">{parrafos}
<div class="btns"><a class="btn b-wa" href="{WA_CONSULTA}">Solicitar una valoración</a><a class="btn b-az" href="/#servicios">Ver todos los servicios</a></div>
<a class="volver" href="/">← Volver al inicio</a></div></div></section>
<section class="alt"><div class="wrap"><h2>Otros programas</h2>{programas_html()}</div></section>'''}

HERRAMIENTAS = [m for m in SITIO['menu'] if m[0] == 'Funcionarios'][0][1][:-1]
def funcionarios():
    tarjetas = ''
    for it in HERRAMIENTAS:
        t, h = it[0], it[1]; d = it[2] if len(it) > 2 else ('Herramienta en línea' if 'reinaelizabeth.com' not in h else 'Herramienta interna')
        ext = ' target="_blank" rel="noopener"'
        cls = 'acceso destacado' if t == 'Agenda-IA' else 'acceso'
        tarjetas += f'<a class="{cls}" href="{h}"{ext}><span class="ico">{t[:2].upper()}</span><span><b>{t}</b><small>{d}</small></span></a>'
    return {'ruta': 'funcionarios/index.html', 'titulo': 'Funcionarios · Reina Elizabeth IPS', 'descripcion': 'Herramientas de trabajo para el equipo de Reina Elizabeth IPS.', 'activo': '', 'cuerpo': f'''
<div class="hero"><div class="wrap"><span class="etq">Equipo de trabajo</span><h1>Funcionarios</h1><p>Herramientas de trabajo del equipo de Reina Elizabeth IPS. La agenda de tareas es Agenda-IA.</p></div></div>
<section><div class="wrap"><div class="accesos">{tarjetas}</div>
<p class="sub-t" style="margin-top:18px">¿Necesita ayuda con alguna herramienta? Use <a href="{RAIZ}/osticketsoportealcliente/scp/login.php" target="_blank" rel="noopener">Soporte y asistencia</a>.</p></div></section>'''}

EDUCACION = {'ruta': 'educacion/index.html', 'titulo': 'Educación y docencia · Reina Elizabeth IPS', 'descripcion': 'Eventos académicos y tests de autoevaluación de Reina Elizabeth IPS.', 'cuerpo': f'''
<div class="hero"><div class="wrap"><span class="etq">Educación y docencia</span><h1>Educación y docencia</h1><p>Eventos académicos y herramientas de autoevaluación para la comunidad.</p></div></div>
<section id="eventos"><div class="wrap"><div class="dos"><div><h2>Eventos académicos</h2><div class="box"><div data-bloque="eventos"><p style="color:var(--suave)">Pronto anunciaremos nuevos eventos.</p></div></div>
<h3 style="margin-top:22px">Documentos</h3><ul class="docs" data-carpeta="academicos"></ul></div>
<aside><h2>Test atencionales</h2><div class="accesos" style="grid-template-columns:1fr">
<a class="acceso" href="{RAIZ}/test-deficit-atencional.html" target="_blank" rel="noopener"><span class="ico">TA</span><span><b>Test Atencional Básico</b><small>Autoevaluación de atención</small></span></a>
<a class="acceso" href="{RAIZ}/mapasueno/mapasueno" target="_blank" rel="noopener"><span class="ico">MS</span><span><b>Mapa de Sueño</b><small>Dificultades para dormir</small></span></a>
<a class="acceso" href="{RAIZ}/atencionyvigiliatest/atencionyvigiliatest" target="_blank" rel="noopener"><span class="ico">AV</span><span><b>Test Atención y Vigilia</b><small>Atención sostenida</small></span></a>
<a class="acceso" href="{RAIZ}/memoria/memoria" target="_blank" rel="noopener"><span class="ico">TM</span><span><b>Test de Memoria</b><small>Evaluación integral de la memoria</small></span></a>
</div><p class="sub-t" style="margin-top:12px;font-size:.88rem">Los tests son orientativos y no reemplazan una valoración profesional.</p></aside></div></div></section>'''}

INSTITUCION = {'ruta': 'institucion/index.html', 'titulo': 'Nuestra institución · Reina Elizabeth IPS', 'descripcion': 'Quiénes somos, SG-SST y trabaja con nosotros.', 'cuerpo': f'''
<div class="hero"><div class="wrap"><span class="etq">Nuestra institución</span><h1>Reina Elizabeth IPS</h1><p>Cuidamos tu salud con amor y fe.</p></div></div>
<section><div class="wrap"><div class="foto-texto"><div><h2>Quiénes somos</h2>
<p>Reina Elizabeth IPS es una institución prestadora de servicios de salud en Santa Marta (Magdalena), con urgencias médicas las 24 horas, medicina general en la IPS y a domicilio, enfermería, vacunación especializada, psicología, terapias y un centro especializado en autismo y neurodivergencia (Autism Center).</p>
<p><b>Visión al 2030:</b> ser un centro de excelencia en servicios de salud de alta complejidad.</p>
<p style="color:var(--suave);font-size:.92rem">Razón social: MONTECARLO SHAIO CLÍNICA IPS S.A.S., sigla Reina Elizabeth IPS · NIT 901074496 · Vigilado Supersalud.</p></div>
<img src="/img/recepcion.jpg" alt="Recepción de Reina Elizabeth IPS" loading="lazy"></div></div></section>
<section class="alt" id="sgsst"><div class="wrap"><h2>SG-SST</h2><p class="sub-t">Sistema de Gestión de Seguridad y Salud en el Trabajo: políticas, matrices y documentos.</p><ul class="docs" data-carpeta="sgsst"></ul>
<h3 style="margin-top:24px">Documentos institucionales</h3><ul class="docs" data-carpeta="institucional"></ul>
<h3 style="margin-top:24px">Formatos para usuarios</h3><ul class="docs" data-carpeta="formatos"></ul></div></section>
<section id="trabaja"><div class="wrap"><h2>Trabaja con nosotros</h2><p class="sub-t">¿Quiere ser parte de nuestro equipo? Envíenos su hoja de vida indicando el cargo de su interés.</p>
<div class="btns"><a class="btn b-az" href="mailto:contacto@reinaelizabeth.com?subject=Hoja%20de%20vida">Enviar hoja de vida</a><a class="btn b-wa" href="https://wa.me/{WA}?text=Hola%2C%20quiero%20trabajar%20con%20Reina%20Elizabeth%20IPS">Escribir por WhatsApp</a></div></div></section>
<section class="alt"><div class="wrap"><h2>Soporte y asistencia</h2><p class="sub-t">Reporte solicitudes de soporte a nuestro sistema de atención.</p><div class="btns"><a class="btn b-az" href="{RAIZ}/osticketsoportealcliente/scp/login.php" target="_blank" rel="noopener">Ir a OsTicket</a></div></div></section>'''}

NOTICIAS = {'ruta': 'noticias/index.html', 'titulo': 'Noticias · Reina Elizabeth IPS', 'descripcion': 'Noticias, eventos y videos de Reina Elizabeth IPS.', 'activo': '/noticias/', 'cuerpo': '''
<div class="hero"><div class="wrap"><span class="etq">Noticias</span><h1>Noticias y eventos</h1><p>Lo que pasa en Reina Elizabeth IPS.</p></div></div>
<section><div class="wrap"><div class="dos"><div data-bloque="noticias-todas"></div><aside><div class="box"><h2 style="font-size:1.4rem">Eventos</h2><div data-bloque="eventos"><p style="color:var(--suave)">Pronto anunciaremos nuevos eventos.</p></div></div></aside></div></div></section>
<section id="videos" class="alt"><div class="wrap"><h2>Videos</h2><div class="videos" data-bloque="videos-todos"></div></div></section>'''}

PAGINAS = [
    {'ruta': 'index.html', 'titulo': 'Reina Elizabeth IPS · Cuidamos tu salud con amor y fe', 'descripcion': 'IPS en Santa Marta: urgencias médicas 24 horas, medicina general en la IPS y a domicilio, enfermería, vacunación, psicología, terapias y programa de autismo y neurodivergencia.', 'cuerpo': INICIO, 'activo': '/'},
    *[programa(*p) for p in PROGRAMAS], funcionarios(), EDUCACION, INSTITUCION, NOTICIAS,
]
