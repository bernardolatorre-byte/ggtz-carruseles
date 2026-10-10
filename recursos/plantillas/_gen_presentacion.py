# Carrusel de presentación de Bernardo Latorre (Pre-*), 10 oct 2026
import importlib.util, pathlib, io, contextlib
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("base", HERE / "_gen_oct20_22.py")
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)
page, foot, polaroid, tape, cierre, sello = base.page, base.foot, base.polaroid, base.tape, base.cierre, base.sello
base.IMG.update(colega="4d623ee1f9fdf083e493b1b0adcdb71b", 
    oficina="df12d7834689b02a85e1e7c7bb293a70", campana="4ead5090323fb1e8ec01f1ce6a258d51",
    caso="af1d182640088e390fc9a1587aeb8853", deloitte1="8a7c7dc900ab04139254ce465038f1e8",
    deloitteeq="be23a7eba4eddb0405ca1c089fe0f071", cumple="ef7401e5a2d861f0e9589b54aa26a24c",
    foropose="3fe85b200d3b7acd10e189542208fef2", termo="1f8dc3829c55597e9446e20484a1c9ab",
    icpnl="a2422d80cf89486e9000c552c64f9d5f", bandera="2f83584efd5212cf53d3f370478a98a0", cerro="e448a584e362be7c35d718376ddbb2a9")
B = base.B
T = 8
S = {}

# 1 · Portada: foto de Bernardo a todo lo ancho
S["Pre-01-Portada"] = page("Presentación · Portada", "", "#F4F1EA", f"""
<img src="{B('oficina')}" alt="Bernardo Latorre en su oficina en Monterrey" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 20%">
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(38,47,59,0) 35%, rgba(38,47,59,0.75) 62%, rgba(38,47,59,0.97) 100%)"></div>
<div style="position: absolute; left: 70px; top: 70px; padding: 12px 22px; background: rgba(244,241,234,0.94); color: #2B3542; font-size: 20px; font-weight: 700; letter-spacing: 0.24em">PRESENTACIÓN</div>
<div style="position: absolute; left: 80px; right: 80px; top: 900px; display: flex; flex-direction: column; gap: 22px">
<h1 class="serif" style="margin: 0; font-size: 140px; line-height: 0.88">Bernardo <em style="font-style: italic; color: #B7CFE6">Latorre</em></h1>
<div style="width: 140px; height: 3px; background: #B7CFE6"></div>
<p style="margin: 0; font-size: 32px; line-height: 1.4; font-weight: 500">Contador Público · Socio de GGTZ Consultores</p>
</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 50px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600; color: rgba(244,241,234,0.8)"><span>@bernardolatorre.fiscal</span><span>Desliza →</span></div>
""")

# 2 · Quién soy: foto grande a la derecha
S["Pre-02-Quien"] = page("Presentación · Perfil", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; right: 0; top: 0; width: 500px; height: 1350px; overflow: hidden">
<img src="{B('icpnl')}" alt="Bernardo Latorre en el ICPNL" style="width: 100%; height: 100%; object-fit: cover; object-position: 22% 40%">
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(38,47,59,0.9) 0%, rgba(38,47,59,0) 35%)"></div>
</div>
<div style="position: absolute; left: 80px; top: 120px; width: 470px; display: flex; flex-direction: column; gap: 30px">
<div class="kicker" style="color: #B7CFE6">PERFIL</div>
<h2 class="serif" style="margin: 0; font-size: 86px; line-height: 0.94">Asesoría fiscal <em style="font-style: italic; color: #B7CFE6">con experiencia</em></h2>
<p style="margin: 0; font-size: 29px; line-height: 1.5; color: rgba(244,241,234,0.9)"><strong style="color: #F4F1EA">Contador Público</strong> egresado de la UDEM y socio de <strong style="color: #F4F1EA">GGTZ Consultores</strong>, despacho de asesoría fiscal y legal en Monterrey.</p>
<p style="margin: 0; font-size: 29px; line-height: 1.5; color: rgba(244,241,234,0.9)">Especializado en cumplimiento y planeación fiscal para personas físicas y PyMEs.</p>
</div>
<div style="position: absolute; left: 80px; top: 1080px; padding: 14px 24px; background: #F4F1EA; color: #2B3542; font-size: 22px; font-weight: 700; letter-spacing: 0.12em; transform: rotate(-2deg)">MONTERREY, N.L.</div>
{foot('@bernardolatorre.fiscal', 2, T, True)}
""")

# 3 · Trayectoria: línea de tiempo con polaroids
def hito(y, tag, t, d, c="#B7CFE6"):
    return (f'<div style="position: absolute; left: 80px; top: {y}px; width: 540px; display: flex; gap: 26px; align-items: flex-start">'
            f'<div style="width: 36px; height: 36px; border-radius: 50%; background: {c}; border: 5px solid #EEEAE1; box-shadow: 0 0 0 2px #2B3542; flex-shrink: 0; margin-top: 6px"></div>'
            f'<div><div class="kicker" style="font-size: 18px; color: #5F7E9E">{tag}</div><div class="serif" style="font-size: 44px; line-height: 1.05; color: #2B3542; margin-top: 4px">{t}</div><div style="font-size: 24px; line-height: 1.4; color: #3A4552; margin-top: 4px">{d}</div></div></div>')
S["Pre-03-Trayectoria"] = page("Presentación · Trayectoria", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px"><div class="kicker" style="color: #5F7E9E">FORMACIÓN Y EXPERIENCIA</div>
<h2 class="serif" style="margin: 16px 0 0; font-size: 92px; line-height: 0.94; color: #2B3542">Mi <em style="font-style: italic">trayectoria</em></h2></div>
<div aria-hidden="true" style="position: absolute; left: 101px; top: 345px; width: 3px; height: 680px; background: #2B3542"></div>
{hito(360, '2019 · UDEM', 'Contador Público', 'Universidad de Monterrey.')}
{hito(570, '8 AÑOS', 'Big Four', '4 años en Deloitte y 4 en EY.')}
{hito(780, 'HOY', 'GGTZ Consultores', 'Socio (antes Latorre y Asociados).', '#A9C9A9')}
{hito(990, 'EN CURSO', 'Maestría en Impuestos', 'En el IEE.', '#D9B4A8')}
{polaroid('caso', 'ICPNL', 650, 300, 360, 220, 4, '55% 40%', 'Bernardo Latorre en el ICPNL')}
{polaroid('campana', 'Graduación UDEM', 690, 640, 300, 300, -4, '40% 40%', 'Bernardo Latorre tocando la campana en su graduación')}
{tape(760, 624, 140, 5)}
{foot('@bernardolatorre.fiscal', 3, T)}
""")

# 4 · Big Four: número gigante + 3 polaroids
S["Pre-04-BigFour"] = page("Presentación · Big Four", "bg-papel", "#1E242C", f"""
<div class="serif" aria-hidden="true" style="position: absolute; left: 40px; top: 20px; font-size: 640px; line-height: 1; color: #B7CFE6">8</div>
<div style="position: absolute; left: 420px; top: 150px; right: 80px; display: flex; flex-direction: column; gap: 18px">
<div class="kicker" style="color: #5F7E9E">AÑOS EN BIG FOUR</div>
<h2 class="serif" style="margin: 0; font-size: 80px; line-height: 0.95; color: #2B3542">4 en Deloitte, <em style="font-style: italic">4 en EY</em></h2>
<p style="margin: 0; font-size: 29px; line-height: 1.45">En esos años desarrollé un método de trabajo riguroso: revisión detallada, documentación completa y cumplimiento puntual.</p>
</div>
{polaroid('deloitte1', 'Deloitte', 90, 700, 420, 360, -4, '50% 45%', 'Bernardo Latorre en Deloitte')}
{polaroid('deloitteeq', 'Con el equipo', 570, 720, 420, 360, 3, '50% 30%', 'Bernardo Latorre con su equipo')}
{tape(240, 682, 120, -8)}{tape(720, 702, 120, 6, 'rgba(201,143,126,0.8)')}
<div style="position: absolute; left: 80px; right: 80px; top: 1170px; font-size: 29px; line-height: 1.45">Hoy aplico ese mismo estándar con <strong>personas físicas y PyMEs.</strong></div>
{foot('@bernardolatorre.fiscal', 4, T)}
""")

# 5 · GGTZ: qué hacemos (chips)
chips = ["Cumplimiento fiscal (ISR, IVA, DIOT)", "Planeación fiscal", "Asesoría a PyMEs", "Personas físicas y RESICO",
         "Constitución de sociedades", "Contratos", "Registro de marca (IMPI)"]
chip_html = "".join(f'<div style="padding: 20px 28px; background: {"#F4F1EA" if i % 3 == 0 else ("#B7CFE6" if i % 3 == 1 else "#A9C9A9")}; color: #1E242C; font-size: 27px; font-weight: 600; border-radius: 40px; transform: rotate({[-2,1.5,-1,2][i%4]}deg)">{c}</div>' for i, c in enumerate(chips))
S["Pre-05-GGTZ"] = page("Presentación · GGTZ", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div class="kicker" style="color: #B7CFE6">HOY</div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94">GGTZ <em style="font-style: italic; color: #B7CFE6">Consultores</em></h2>
<p style="margin: 0; font-size: 30px; line-height: 1.45; color: rgba(244,241,234,0.88)">Asesoría fiscal y legal desde Monterrey. Lo que hacemos en el despacho:</p>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 470px; display: flex; flex-wrap: wrap; gap: 22px 18px">{chip_html}</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1010px; padding: 36px 40px; border: 2px solid rgba(244,241,234,0.3); transform: rotate(-1deg)">
<div class="kicker" style="font-size: 18px; color: #B7CFE6">DÓNDE ESTAMOS</div>
<div style="font-size: 28px; line-height: 1.4; margin-top: 10px">Torre MOTOMEX, Centro de Negocios · Av. Pino Suárez 750, Monterrey</div></div>
{foot('@bernardolatorre.fiscal', 5, T, True)}
""")

# 6 · Sigo aprendiendo: ICPNL + Foro + IEE
S["Pre-06-Aprendiendo"] = page("Presentación · Comunidad", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 18px">
<div class="kicker" style="color: #5F7E9E">LOS IMPUESTOS CAMBIAN CADA AÑO</div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">Actualización <em style="font-style: italic">constante</em></h2>
</div>
{polaroid('foropose', 'Foro Económico Fiscal', 80, 400, 380, 400, -4, '50% 30%', 'Bernardo Latorre en el Foro Económico Fiscal del ICPNL')}
{polaroid('colega', 'miembro activo del ICPNL', 560, 370, 420, 330, 4, '50% 35%', 'Bernardo Latorre en el ICPNL')}
{polaroid('termo', 'Formación continua', 600, 800, 330, 250, -3, '50% 60%', 'Sesión en el ICPNL')}
<div style="position: absolute; left: 80px; top: 960px; width: 470px; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; gap: 16px; align-items: flex-start"><span class="serif" style="font-size: 44px; line-height: 1; color: #5F7E9E">→</span><span style="font-size: 27px; line-height: 1.4">Miembro activo del <strong>ICPNL</strong></span></div>
<div style="display: flex; gap: 16px; align-items: flex-start"><span class="serif" style="font-size: 44px; line-height: 1; color: #5F7E9E">→</span><span style="font-size: 27px; line-height: 1.4">Cursando la <strong>Maestría en Impuestos</strong> en el IEE</span></div>
</div>
{foot('@bernardolatorre.fiscal', 6, T)}
""")

# 7 · Qué vas a encontrar aquí (post-its)
def postit(t, x, y, rot, bg):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: 420px; min-height: 230px; box-sizing: border-box; padding: 38px 32px; background: {bg}; transform: rotate({rot}deg); box-shadow: 0 16px 26px rgba(43,53,66,0.2); font-size: 29px; line-height: 1.4">{t}</div>'
S["Pre-07-Cuenta"] = page("Presentación · Esta cuenta", "", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 18px">
<div style="align-self: flex-start; padding: 12px 22px; background: #2B3542; color: #F4F1EA; font-size: 20px; font-weight: 700; letter-spacing: 0.2em; transform: rotate(-2deg)">MARTES Y JUEVES</div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #1E242C">Contenido de <em style="font-style: italic">esta cuenta</em></h2>
</div>
{postit('<strong>Temas fiscales</strong> explicados de forma clara.', 80, 480, -3, '#FFFDF8')}
{postit('<strong>Fechas límite</strong> y obligaciones próximas.', 580, 470, 3, '#D6E4F2')}
{postit('<strong>Errores frecuentes</strong> y cómo prevenirlos.', 90, 790, 2, '#CFE3C9')}
{postit('<strong>Reformas y cambios</strong> del SAT, en cuanto se publican.', 590, 780, -2, '#F2D9D0')}
{foot('@bernardolatorre.fiscal', 7, T)}
""", bg=" background: #D9B4A8;")

S["Pre-08-Cierre"] = cierre("Agende una", "asesoría",
    "Atención a personas físicas y empresas en materia fiscal y legal.",
    "Contactar", "Martes y jueves publico contenido fiscal. <strong>Le invito a seguir la cuenta.</strong>",
    "cerro", "50% 58%", 8, T, "Cerro de la Silla al atardecer")

for k, v in S.items():
    (HERE / f"{k}.dc.html").write_text(v)
print(len(S))
