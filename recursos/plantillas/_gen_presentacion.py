# Carrusel de presentación "Hola, soy Berny" (Pre-*), 10 oct 2026
import importlib.util, pathlib, io, contextlib
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("base", HERE / "_gen_oct20_22.py")
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)
page, foot, polaroid, tape, cierre, sello = base.page, base.foot, base.polaroid, base.tape, base.cierre, base.sello
base.IMG.update(
    oficina="df12d7834689b02a85e1e7c7bb293a70", campana="4ead5090323fb1e8ec01f1ce6a258d51",
    caso="af1d182640088e390fc9a1587aeb8853", deloitte1="8a7c7dc900ab04139254ce465038f1e8",
    deloitteeq="be23a7eba4eddb0405ca1c089fe0f071", cumple="ef7401e5a2d861f0e9589b54aa26a24c",
    foropose="3fe85b200d3b7acd10e189542208fef2", termo="1f8dc3829c55597e9446e20484a1c9ab",
    icpnl="a2422d80cf89486e9000c552c64f9d5f", cerro="e448a584e362be7c35d718376ddbb2a9")
B = base.B
T = 8
S = {}

# 1 · Portada: gafete colgando (sin foto de Berny)
S["Pre-01-Portada"] = page("Presentación · Portada", "bg-papel", "#1E242C", f"""
<svg aria-hidden="true" style="position: absolute; left: 0; top: 0" width="1080" height="1350"><path d="M470 0 L520 250 M640 0 L590 250" stroke="#5F7E9E" stroke-width="22" stroke-linecap="round"></path></svg>
<div style="position: absolute; left: 330px; top: 220px; width: 450px; box-sizing: border-box; background: #FFFFFF; border-radius: 22px; overflow: hidden; transform: rotate(-4deg); box-shadow: 0 30px 60px rgba(30,36,44,0.3)">
<div style="height: 26px; width: 110px; margin: 18px auto 0; border-radius: 13px; background: #E9E6DF"></div>
<div style="margin-top: 18px; padding: 16px 0; background: #2B3542; color: #F4F1EA; text-align: center; font-size: 19px; font-weight: 700; letter-spacing: 0.3em">GGTZ CONSULTORES</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 14px; padding: 36px 30px 34px">
<div class="serif" style="width: 170px; height: 170px; border-radius: 50%; background: #B7CFE6; color: #2B3542; display: flex; align-items: center; justify-content: center; font-size: 96px">BL</div>
<div class="serif" style="font-size: 50px; line-height: 1; color: #2B3542; margin-top: 8px">Bernardo Latorre</div>
<div style="font-size: 23px; color: #3A4552">Contador Público · Socio fundador</div>
<svg aria-hidden="true" width="300" height="46" viewBox="0 0 300 46" style="margin-top: 10px"><g fill="#2B3542">{''.join(f'<rect x="{x}" y="0" width="{w}" height="46"></rect>' for x, w in [(0,4),(8,2),(14,6),(24,2),(30,4),(38,8),(50,2),(56,4),(64,2),(70,6),(80,4),(88,2),(94,8),(106,2),(112,4),(120,6),(130,2),(136,4),(144,2),(150,8),(162,4),(170,2),(176,6),(186,2),(192,4),(200,8),(212,2),(218,4),(226,6),(236,2),(242,4),(250,2),(256,8),(268,4),(276,2),(282,6),(292,4)])}</g></svg>
</div></div>
<div style="position: absolute; left: 80px; right: 80px; top: 930px; display: flex; flex-direction: column; gap: 18px">
<h1 class="serif" style="margin: 0; font-size: 156px; line-height: 0.86; color: #2B3542">Hola, soy <em style="font-style: italic">Berny</em></h1>
<p style="margin: 0; font-size: 34px; line-height: 1.35; font-weight: 500">Te cuento quién soy y <span style="background: linear-gradient(transparent 52%, #B7CFE6 52%); padding: 0 6px">cómo llegué hasta aquí</span></p>
</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 50px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600; color: #5F7E9E"><span>@bernardolatorre.fiscal</span><span>Desliza →</span></div>
""")

# 2 · Quién soy: foto grande a la derecha
S["Pre-02-Quien"] = page("Presentación · Quién soy", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; right: 0; top: 0; width: 500px; height: 1350px; overflow: hidden">
<img src="{B('oficina')}" alt="Berny en su oficina en Monterrey" style="width: 100%; height: 100%; object-fit: cover; object-position: 55% 30%">
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(38,47,59,0.9) 0%, rgba(38,47,59,0) 35%)"></div>
</div>
<div style="position: absolute; left: 80px; top: 120px; width: 470px; display: flex; flex-direction: column; gap: 30px">
<div class="kicker" style="color: #B7CFE6">MUCHO GUSTO</div>
<h2 class="serif" style="margin: 0; font-size: 86px; line-height: 0.94">Bernardo Latorre, <em style="font-style: italic; color: #B7CFE6">pero dime Berny</em></h2>
<p style="margin: 0; font-size: 29px; line-height: 1.5; color: rgba(244,241,234,0.9)">Soy <strong style="color: #F4F1EA">Contador Público</strong> y socio fundador de <strong style="color: #F4F1EA">GGTZ Consultores</strong>, un despacho de asesoría fiscal y legal en Monterrey.</p>
<p style="margin: 0; font-size: 29px; line-height: 1.5; color: rgba(244,241,234,0.9)">Me especializo en impuestos: que personas y PyMEs cumplan con el SAT, planeen y paguen lo justo.</p>
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
<div style="position: absolute; left: 80px; top: 96px; right: 80px"><div class="kicker" style="color: #5F7E9E">MI CAMINO</div>
<h2 class="serif" style="margin: 16px 0 0; font-size: 92px; line-height: 0.94; color: #2B3542">Cómo llegué <em style="font-style: italic">hasta aquí</em></h2></div>
<div aria-hidden="true" style="position: absolute; left: 101px; top: 345px; width: 3px; height: 860px; background: #2B3542"></div>
{hito(330, '2017 · ESTUDIANTE', 'Caso ICPNL', 'Tercer lugar en el 14° Caso del Instituto.')}
{hito(530, '2019 · UDEM', 'Contador Público', 'Egresado de la Universidad de Monterrey.')}
{hito(730, '8 AÑOS', 'Big Four', '4 años en Deloitte y 4 en EY.')}
{hito(930, 'HOY', 'GGTZ Consultores', 'Socio fundador (antes Latorre y Asociados).', '#A9C9A9')}
{hito(1110, 'EN CURSO', 'Maestría en Impuestos', 'En el IEE.', '#D9B4A8')}
{polaroid('caso', 'tercer lugar, 2017', 650, 300, 360, 220, 4, '55% 40%', 'Berny recibiendo el tercer lugar del Caso ICPNL 2017')}
{polaroid('campana', 'graduación UDEM', 690, 640, 300, 300, -4, '40% 40%', 'Berny tocando la campana en su graduación')}
{tape(760, 624, 140, 5)}
{foot('@bernardolatorre.fiscal', 3, T)}
""")

# 4 · Big Four: número gigante + 3 polaroids
S["Pre-04-BigFour"] = page("Presentación · Big Four", "bg-papel", "#1E242C", f"""
<div class="serif" aria-hidden="true" style="position: absolute; left: 40px; top: 20px; font-size: 640px; line-height: 1; color: #B7CFE6">8</div>
<div style="position: absolute; left: 420px; top: 150px; right: 80px; display: flex; flex-direction: column; gap: 18px">
<div class="kicker" style="color: #5F7E9E">AÑOS EN BIG FOUR</div>
<h2 class="serif" style="margin: 0; font-size: 80px; line-height: 0.95; color: #2B3542">4 en Deloitte, <em style="font-style: italic">4 en EY</em></h2>
<p style="margin: 0; font-size: 29px; line-height: 1.45">Ahí aprendí cómo se trabaja con rigor: revisar cada cifra, documentar todo y cumplir fechas sin excusas.</p>
</div>
{polaroid('deloitte1', 'primeros años', 70, 720, 300, 280, -6, '50% 45%', 'Berny en el lobby de Deloitte')}
{polaroid('deloitteeq', 'el equipo', 390, 760, 300, 280, 3, '50% 30%', 'Berny con compañeros en un evento')}
{polaroid('cumple', 'cumpleaños en la oficina', 710, 720, 300, 280, -2, '40% 40%', 'Festejo de cumpleaños en su escritorio')}
{tape(160, 700, 120, -8)}{tape(800, 700, 120, 6, 'rgba(201,143,126,0.8)')}
<div style="position: absolute; left: 80px; right: 80px; top: 1130px; font-size: 29px; line-height: 1.45">Hoy llevo esa misma forma de trabajar <strong>a personas y PyMEs.</strong></div>
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
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">Por eso <em style="font-style: italic">sigo estudiando</em></h2>
</div>
{polaroid('foropose', 'Foro Económico Fiscal', 80, 400, 380, 400, -4, '50% 30%', 'Berny en el Foro Económico Fiscal del ICPNL')}
{polaroid('icpnl', 'miembro activo del ICPNL', 560, 370, 420, 330, 4, '25% 35%', 'Berny frente al logo del ICPNL')}
{polaroid('termo', 'cursos y sesiones', 600, 800, 330, 250, -3, '50% 60%', 'Sesión en el ICPNL')}
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
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #1E242C">Qué vas a encontrar <em style="font-style: italic">en esta cuenta</em></h2>
</div>
{postit('<strong>Impuestos explicados</strong> en sencillo, sin tecnicismos.', 80, 480, -3, '#FFFDF8')}
{postit('<strong>Fechas límite</strong> para que no se te pase nada.', 580, 470, 3, '#D6E4F2')}
{postit('<strong>Errores comunes</strong> que veo en el despacho y cómo evitarlos.', 90, 790, 2, '#CFE3C9')}
{postit('<strong>Cambios del SAT</strong> y de la ley, en cuanto salen.', 590, 780, -2, '#F2D9D0')}
{foot('@bernardolatorre.fiscal', 7, T)}
""", bg=" background: #D9B4A8;")

S["Pre-08-Cierre"] = cierre("¿En qué te", "puedo ayudar?",
    "Si tienes dudas con el SAT, tu negocio o tus impuestos, platiquemos.",
    "Agenda tu asesoría", "<strong>Cuéntame en comentarios</strong> qué tema quieres que explique primero. Y sígueme para no perderte nada.",
    "cerro", "50% 58%", 8, T, "Cerro de la Silla al atardecer")

for k, v in S.items():
    (HERE / f"{k}.dc.html").write_text(v)
print(len(S))
