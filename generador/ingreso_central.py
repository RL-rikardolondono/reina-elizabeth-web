# Convierte el panel /admin (modelo POLIANDES, usuarios cifrados en el repositorio) al
# SERVICIO CENTRAL DE INGRESO de SkyNet Genesis (skynetgenesis.com/ingreso/api.php):
# correo + contraseña, "¿Olvidó su contraseña?" por enlace al correo, y la llave de GitHub
# guardada cifrada en el servidor (se pega una sola vez). Directiva general de webs.
# Mismo archivo en reina-elizabeth-web y anglocolombiano-web.

SITIOS = {
    'reina-elizabeth-web': ('reinaelizabeth', 'contacto@reinaelizabeth.com'),
    'anglocolombiano-web': ('anglocolombiano', 'anglo@anglocolombiano.com'),
}

HTML = '''<!-- INGRESO -->
  <section id="vista-ingreso" class="ingreso">
    <div class="caja" id="caja-entrar">
      <h1>Entrar al panel</h1>
      <p>Entre con su correo y su contraseña del panel.</p>
      <label for="ing-correo">Correo</label>
      <input type="email" id="ing-correo" autocomplete="username">
      <label for="ing-clave">Contraseña</label>
      <input type="password" id="ing-clave" autocomplete="current-password">
      <label class="chk"><input type="checkbox" id="recordar" checked> Recordar en este equipo (no lo marque en computadores ajenos)</label>
      <div id="aviso-ingreso"></div>
      <div class="pie-acciones"><button class="boton b-principal b-grande" id="btn-entrar" type="button">Entrar</button></div>
      <p class="ayuda" style="margin-top:14px"><a href="#" id="btn-olvido">¿Olvidó su contraseña?</a> · <a href="#" id="btn-primera">¿Primera vez? Crear mi contraseña</a></p>
      <p class="ayuda">Soporte: SkyNet Genesis · contacto@skynetgenesis.com · WhatsApp 3044375758</p>
    </div>

    <div class="caja oculto" id="caja-nueva">
      <h1>Crear nueva contraseña</h1>
      <p>Escriba su nueva contraseña del panel (mínimo 8 caracteres).</p>
      <label for="nueva-clave">Nueva contraseña</label>
      <input type="password" id="nueva-clave" autocomplete="new-password">
      <label for="nueva-clave2">Repita la contraseña</label>
      <input type="password" id="nueva-clave2" autocomplete="new-password">
      <div id="aviso-nueva"></div>
      <div class="pie-acciones"><button class="boton b-principal b-grande" id="btn-clave-nueva" type="button">Guardar y entrar</button></div>
    </div>

    <div class="caja oculto" id="caja-llave">
      <h1>Configuración inicial (solo una vez)</h1>
      <p>Para que el panel pueda publicar en la web, GitHub necesita una llave de acceso. Se pega <b>una sola vez</b>: queda guardada de forma segura en el servidor y nadie tendrá que volver a verla.</p>
      <ol class="pasos">
        <li>Inicie sesión en GitHub y abra <a href="https://github.com/settings/personal-access-tokens/new" target="_blank" rel="noopener">esta página</a>.</li>
        <li>En <b>Token name</b> escriba: <i>Panel __NOMBRE__</i>. En <b>Expiration</b> elija <b>No expiration</b>.</li>
        <li>En <b>Repository access</b> elija <b>Only select repositories</b> y marque solo <b>__REPO__</b>.</li>
        <li>En <b>Permissions → Repository permissions</b>, ponga <b>Contents</b> en <b>Read and write</b>. Nada más.</li>
        <li>Pulse <b>Generate token</b>, copie la llave (empieza por <code>github_pat_</code>) y péguela aquí abajo.</li>
      </ol>
      <label for="llave">Llave de GitHub</label>
      <input type="password" id="llave" autocomplete="off" placeholder="github_pat_…">
      <div id="aviso-llave"></div>
      <div class="pie-acciones"><button class="boton b-principal b-grande" id="btn-llave" type="button">Guardar y entrar</button></div>
    </div>
  </section>

  '''

JS = r'''/* ---------- Ingreso (correo y contraseña por el servicio central de SkyNet Genesis) ---------- */
function api(accion, datos) {
  datos = datos || {}; datos.sitio = CONFIG.sitioId; datos.accion = accion;
  return fetch(CONFIG.ingreso + '?sitio=' + encodeURIComponent(CONFIG.sitioId), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(datos), cache: 'no-store' })
    .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || !j.ok) { var e = new Error(j.error || 'No se pudo conectar con el servicio de ingreso. Intente de nuevo.'); e.status = r.status; throw e; } return j; }); },
          function () { throw new Error('No hay conexión a internet. Intente de nuevo.'); });
}
function verCaja(id) { ['caja-entrar', 'caja-nueva', 'caja-llave'].forEach(function (c) { $(c).classList.toggle('oculto', c !== id); }); $('vista-ingreso').classList.remove('oculto'); }
function guardarSesion(s, recordar) { borrarLS(CONFIG.claveLocal); guardarLS(CONFIG.claveLocal, s, recordar); }
function trasIngreso(r) {
  if (!r.configurado || !r.llave) { cargando(false); verCaja('caja-llave'); return; }
  cargarPanel(r.llave);
}
function cargarPanel(llave) {
  estado.llave = llave;
  cargando(true, 'Entrando…');
  gh('').then(function (repo) {
    if (repo.permissions && !repo.permissions.push) throw errorGH(403);
    return Promise.all([refActual(), leerArchivo(CONFIG.datos)]);
  }).then(function (r) {
    estado.commitBase = r[0];
    estado.datos = JSON.parse(r[1]);
    ['noticias', 'eventos', 'videos', 'galeria'].forEach(function (k) { if (!estado.datos[k]) estado.datos[k] = []; });
    $('vista-ingreso').classList.add('oculto'); $('vista-panel').classList.remove('oculto'); $('acciones-barra').classList.remove('oculto');
    cargando(false); pintarTodo();
  }).catch(function (e) {
    cargando(false); estado.llave = '';
    if (e.status === 401 || e.status === 403 || e.status === 404) { verCaja('caja-llave'); aviso('aviso-llave', 'error', 'La llave de GitHub guardada ya no funciona (' + e.message + ') Cree una nueva y péguela aquí.'); return; }
    verCaja('caja-entrar'); aviso('aviso-ingreso', 'error', e.message);
  });
}
$('ing-correo').value = CONFIG.correo;
$('btn-entrar').onclick = function () {
  var correo = $('ing-correo').value.trim(), clave = $('ing-clave').value, recordar = $('recordar').checked;
  if (!correo || !clave) { aviso('aviso-ingreso', 'error', 'Escriba su correo y su contraseña.'); return; }
  cargando(true, 'Entrando…'); aviso('aviso-ingreso', '', '');
  api('entrar', { correo: correo, clave: clave, recordar: recordar }).then(function (r) {
    $('ing-clave').value = ''; guardarSesion(r.sesion, recordar); trasIngreso(r);
  }).catch(function (e) { cargando(false); aviso('aviso-ingreso', 'error', e.message); });
};
$('ing-clave').addEventListener('keydown', function (e) { if (e.key === 'Enter') $('btn-entrar').click(); });
function pedirEnlace(ev) {
  ev.preventDefault();
  var correo = $('ing-correo').value.trim();
  if (!correo) { aviso('aviso-ingreso', 'error', 'Escriba primero su correo.'); return; }
  cargando(true, 'Enviando el correo…');
  api('solicitar', { correo: correo }).then(function () {
    cargando(false);
    aviso('aviso-ingreso', 'ok', 'Listo. Si ese correo tiene acceso al panel, le llegará en unos minutos un mensaje con un enlace para crear su contraseña. Revise también la carpeta de spam. El enlace vence en 1 hora.');
  }).catch(function (e) { cargando(false); aviso('aviso-ingreso', 'error', e.message); });
}
$('btn-olvido').onclick = pedirEnlace;
$('btn-primera').onclick = pedirEnlace;
$('btn-clave-nueva').onclick = function () {
  var c1 = $('nueva-clave').value, c2 = $('nueva-clave2').value;
  if (c1.length < 8) { aviso('aviso-nueva', 'error', 'La contraseña debe tener al menos 8 caracteres.'); return; }
  if (c1 !== c2) { aviso('aviso-nueva', 'error', 'Las dos contraseñas no coinciden.'); return; }
  var codigo = (location.hash.match(/clave=([a-f0-9]+)/) || [])[1] || '';
  cargando(true, 'Guardando…');
  api('fijar', { codigo: codigo, clave: c1, recordar: true }).then(function (r) {
    history.replaceState(null, '', location.pathname);
    $('nueva-clave').value = $('nueva-clave2').value = '';
    guardarSesion(r.sesion, true); trasIngreso(r);
  }).catch(function (e) { cargando(false); aviso('aviso-nueva', 'error', e.message); });
};
$('btn-llave').onclick = function () {
  var llave = $('llave').value.trim();
  if (!/^(github_pat_|ghp_)/.test(llave)) { aviso('aviso-llave', 'error', 'Eso no parece una llave de GitHub. Debe empezar por «github_pat_».'); return; }
  cargando(true, 'Comprobando la llave…');
  api('guardar_llave', { sesion: leerLS(CONFIG.claveLocal), llave: llave }).then(function (r) {
    $('llave').value = ''; cargarPanel(r.llave);
  }).catch(function (e) {
    cargando(false);
    if (e.status === 401) { borrarLS(CONFIG.claveLocal); verCaja('caja-entrar'); aviso('aviso-ingreso', 'error', e.message); return; }
    aviso('aviso-llave', 'error', e.message);
  });
};
$('btn-salir').onclick = function () {
  if (estado.cambiosSinGuardar && !confirm('Tiene cambios sin publicar. ¿Salir de todos modos?')) return;
  var s = leerLS(CONFIG.claveLocal); borrarLS(CONFIG.claveLocal); estado.cambiosSinGuardar = false;
  (s ? api('salir', { sesion: s }).catch(function () {}) : Promise.resolve()).then(function () { location.reload(); });
};
window.addEventListener('beforeunload', function (e) { if (estado.cambiosSinGuardar) { e.preventDefault(); e.returnValue = ''; } });
(function () {
  window.addEventListener('hashchange', function () { if (/clave=[a-f0-9]+/.test(location.hash)) { $('vista-panel').classList.add('oculto'); $('acciones-barra').classList.add('oculto'); verCaja('caja-nueva'); } });
  borrarLS(CONFIG.claveLocalVieja); // limpia la llave que antes se guardaba en el equipo
  if (/clave=[a-f0-9]+/.test(location.hash)) { verCaja('caja-nueva'); return; }
  var s = leerLS(CONFIG.claveLocal);
  if (!s) { verCaja('caja-entrar'); return; }
  cargando(true, 'Entrando…');
  api('sesion', { sesion: s }).then(trasIngreso).catch(function (e) {
    cargando(false); if (e.status === 401) borrarLS(CONFIG.claveLocal);
    verCaja('caja-entrar'); if (e.status !== 401) aviso('aviso-ingreso', 'error', e.message);
  });
})();

'''


def convertir(p, c):
    sitio_id, correo = SITIOS[c['repo']]
    a, b = p.index('<!-- INGRESO -->'), p.index('<!-- PANEL -->')
    p = p[:a] + HTML.replace('__NOMBRE__', c['nombre_corto']).replace('__REPO__', c['repo']) + p[b:]
    a, b = p.index('/* ---------- Ingreso ---------- */'), p.index('/* ---------- Pestañas ---------- */')
    p = p[:a] + JS + p[b:]
    vieja = f"panel-{c['repo']}-llave"
    p = p.replace(f"claveLocal: '{vieja}',",
                  f"claveLocal: 'panel-{c['repo']}-sesion',\n  claveLocalVieja: '{vieja}',\n"
                  f"  sitioId: '{sitio_id}',                       // nombre de esta web en el servicio de ingreso\n"
                  f"  correo: '{correo}',            // correo que entra al panel\n"
                  f"  ingreso: 'https://skynetgenesis.com/ingreso/api.php',   // servicio central de ingreso de SkyNet Genesis", 1)
    # Los usuarios ahora los maneja el servicio central: se quita la pestaña «Usuarios»
    p = p.replace('<button class="pestana" role="tab" aria-selected="false" data-pestana="usuarios">Usuarios</button>', '')
    p = p.replace('<script src="/admin/acceso.js"></script>\n', '')
    p = p.replace("['llave', 'i-correo', 'i-clave',", "['llave', 'ing-correo', 'ing-clave', 'nueva-clave', 'nueva-clave2',")
    for x in ["sitioId: '", 'id="btn-olvido"', 'function cargarPanel', 'claveLocalVieja']:
        if x not in p: raise SystemExit('ERROR ingreso central: falta ' + x)
    return p
