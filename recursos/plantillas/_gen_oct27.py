# Carrusel "Tus primeros clientes como contador" (Cli-*), idea de Berny (ref. @cooltura.fiscal)
import importlib.util, pathlib, sys, io, contextlib
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("base", HERE / "_gen_oct20_22.py")
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)
page, foot, polaroid, tape, cierre, num_badge = base.page, base.foot, base.polaroid, base.tape, base.cierre, base.num_badge
base.IMG.update(cafe="cb53358cbd5f1694569d50016950c96f", florista="42d8079cc3c861ee4b89735b38496096",
                mecanico="5dbe984a94857f880f3988204f66fcb3", barberia="cab0e08a0c98b670f1eccfaacfa36c4c",
                sathome="0adc0a675d66cb76d2f8d28aa693463f", cerro="e448a584e362be7c35d718376ddbb2a9",
                deloitte2="a011b9480cdaf80932f25a89e006f0e7", deloitteeq="be23a7eba4eddb0405ca1c089fe0f071",
                oficina="df12d7834689b02a85e1e7c7bb293a70", icpnl="a2422d80cf89486e9000c552c64f9d5f", foro="5f30980ae63e1c1aea6b4d1660223e2f")
B = base.B
T = 9
S = {}

def head(n, kicker, title, dark=False, right=80):
    kc = "#B7CFE6" if dark else "#5F7E9E"; tc = "" if dark else "color: #2B3542;"
    return (f'<div style="position: absolute; left: 80px; top: 96px; right: {right}px; display: flex; flex-direction: column; gap: 22px">'
            f'<div style="display: flex; align-items: center; gap: 26px">{num_badge(n, dark)}<div class="kicker" style="color: {kc}">{kicker}</div></div>'
            f'<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; {tc}">{title}</h2></div>')

# 1 · Portada: salvia liso, título centrado, ruta punteada Big Four -> despacho propio
S["Cli-01-Portada"] = page("Primeros clientes · Portada", "", "#1E242C", f"""
<svg aria-hidden="true" style="position: absolute; left: 0; top: 0" width="1080" height="1350"><path d="M150 1130 C 330 1010, 260 900, 470 880 S 760 980, 930 820" fill="none" stroke="#2B3542" stroke-width="5" stroke-dasharray="4 18" stroke-linecap="round"></path></svg>
<div style="position: absolute; left: 80px; right: 80px; top: 150px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 30px">
<div style="padding: 12px 24px; background: #FFFDF8; color: #2B3542; font-size: 20px; font-weight: 700; letter-spacing: 0.2em; transform: rotate(-2deg)">PARA COLEGAS QUE EMPIEZAN</div>
<h1 class="serif" style="margin: 0; font-size: 150px; line-height: 0.86; color: #1E242C">Tus primeros <em style="font-style: italic">clientes</em> como contador</h1>
<p style="margin: 0; max-width: 760px; font-size: 34px; line-height: 1.35; font-weight: 500">6 cosas que recomiendo después de 8 años en Big Four y de abrir mi propio despacho</p>
</div>
<div style="position: absolute; left: 70px; top: 1100px; padding: 18px 26px; background: #2B3542; color: #F4F1EA; font-size: 24px; font-weight: 700; transform: rotate(-4deg); box-shadow: 0 12px 24px rgba(30,36,44,0.25)">Big Four</div>
<div class="sticker" style="position: absolute; left: 820px; top: 720px; transform: rotate(6deg)"><svg role="img" aria-label="Pin de llegada" width="130" height="160" viewBox="0 0 26 32"><path d="M13 31s11-11 11-18A11 11 0 0 0 2 13c0 7 11 18 11 18z" fill="#C98F7E"></path><circle cx="13" cy="13" r="4.5" fill="#FFFDF8"></circle></svg></div>
<div style="position: absolute; left: 700px; top: 900px; padding: 18px 26px; background: #FFFDF8; color: #2B3542; font-size: 24px; font-weight: 700; transform: rotate(3deg); box-shadow: 0 12px 24px rgba(30,36,44,0.18)">Tu propio despacho</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 60px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600; color: #2B3542"><span>GGTZ Consultores · @bernardolatorre.fiscal</span><span>Desliza →</span></div>
""", bg=" background: #A9C9A9;")

# 2 · Intro: cita grande en oscuro
S["Cli-02-Intro"] = page("Primeros clientes · Intro", "bg-sarga", "#F4F1EA", f"""
<div class="serif" aria-hidden="true" style="position: absolute; left: 50px; top: 10px; font-size: 520px; line-height: 1; color: rgba(183,207,230,0.18)">“</div>
{polaroid('deloitte2', 'mis años en Big Four', 690, 80, 320, 300, 5, '50% 50%', 'Berny en el lobby de Deloitte')}
{tape(790, 62, 140, -5)}
<div style="position: absolute; left: 80px; right: 80px; top: 500px; display: flex; flex-direction: column; gap: 40px">
<p class="serif" style="margin: 0; font-size: 80px; line-height: 1.02">Independizarte da miedo. <em style="font-style: italic; color: #B7CFE6">El primer cliente es el que más cuesta.</em></p>
<div style="width: 120px; height: 4px; background: #B7CFE6"></div>
<p style="margin: 0; max-width: 820px; font-size: 32px; line-height: 1.5; color: rgba(244,241,234,0.88)">No hay fórmula mágica, pero sí cosas que puedes empezar a hacer hoy para que la gente te conozca <strong style="color: #F4F1EA">y te tenga confianza.</strong></p>
<p style="margin: 0; font-size: 26px; font-weight: 600; letter-spacing: 0.04em; color: #B7CFE6">— Berny, GGTZ Consultores</p>
</div>
{foot('@bernardolatorre.fiscal', 2, T, True)}
""")

# 3 · Círculos concéntricos
def ring(d, color, label, ly):
    return (f'<div style="position: absolute; left: {540 - d // 2}px; top: {950 - d // 2}px; width: {d}px; height: {d}px; border-radius: 50%; background: {color}; border: 2px solid rgba(43,53,66,0.25)"></div>'
            f'<div style="position: absolute; left: 0; right: 0; top: {ly}px; text-align: center; font-size: 25px; font-weight: 600; color: #2B3542">{label}</div>')
S["Cli-03-Circulos"] = page("Primeros clientes · Quién te conoce", "bg-lino", "#1E242C", f"""
{head(1, 'EMPIEZA CERCA', 'Con quien <em style="font-style: italic">ya te conoce</em>', False, 400)}
{polaroid('deloitteeq', 'excompañeros', 720, 70, 290, 230, 5, '50% 30%', 'Berny con compañeros de Deloitte')}
<p style="position: absolute; left: 80px; right: 80px; top: 450px; margin: 0; font-size: 30px; line-height: 1.45">Tu primer cliente casi siempre está más cerca de lo que crees. Cuéntales qué haces y en qué les puedes ayudar.</p>
{ring(620, '#FFFDF8', 'Conocidos de conocidos', 665)}{ring(440, '#D6E4F2', 'Excompañeros de trabajo', 755)}{ring(260, '#B7CFE6', 'Familia y amigos', 845)}
<div style="position: absolute; left: 470px; top: 910px; width: 140px; height: 80px; border-radius: 40px; background: #2B3542; color: #F4F1EA; display: flex; align-items: center; justify-content: center; font-size: 30px; font-weight: 700">Tú</div>
{foot('@bernardolatorre.fiscal', 3, T)}
""")

# 4 · Tarjetas de presentación + nichos
S["Cli-04-Nicho"] = page("Primeros clientes · Nicho", "bg-papel", "#1E242C", f"""
{head(2, 'ELIGE A QUIÉN AYUDAS', 'No ofrezcas <em style="font-style: italic">de todo</em>')}
<div style="position: absolute; left: 80px; top: 380px; width: 560px; height: 300px; box-sizing: border-box; padding: 40px; background: #FFFFFF; border-radius: 12px; transform: rotate(-4deg); box-shadow: 0 16px 30px rgba(30,36,44,0.18); display: flex; flex-direction: column; justify-content: space-between">
<div><div class="serif" style="font-size: 44px; color: #2B3542">Juan Pérez</div><div style="font-size: 26px; color: #3A4552; margin-top: 8px">Contador. Hago de todo.</div></div>
<div style="font-size: 20px; color: #8A94A0">Tel. 00 0000 0000</div></div>
<div aria-hidden="true" style="position: absolute; left: 60px; top: 520px; width: 620px; height: 8px; background: #C98F7E; transform: rotate(-14deg); border-radius: 4px"></div>
<div style="position: absolute; right: 80px; top: 560px; width: 600px; box-sizing: border-box; padding: 40px; background: #2B3542; color: #F4F1EA; border-radius: 12px; transform: rotate(3deg); box-shadow: 0 20px 36px rgba(30,36,44,0.28)">
<div class="serif" style="font-size: 44px">Juan Pérez</div>
<div style="font-size: 27px; line-height: 1.4; margin-top: 10px">Ayudo a <span style="color: #B7CFE6; font-weight: 700">talleres y barberías</span> a estar al día con el SAT sin perder horas de trabajo.</div></div>
<div style="position: absolute; left: 80px; top: 890px; font-size: 28px; line-height: 1.45; width: 900px">Es más fácil que te recomienden si saben <strong>exactamente</strong> qué haces y para quién.</div>
{polaroid('mecanico', 'talleres', 120, 1005, 230, 150, -5, '50% 35%', 'Mecánico trabajando')}
{polaroid('barberia', 'barberías', 420, 995, 230, 150, 3, '60% 30%', 'Barbería')}
{polaroid('florista', 'florerías', 720, 1010, 230, 150, -2, '35% 45%', 'Florista en su puesto')}
{foot('@bernardolatorre.fiscal', 4, T)}
""")

# 5 · Calendario semanal de contenido
def day(d, t, bg, fg, rot):
    return f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 14px; padding: 26px 20px; background: {bg}; color: {fg}; transform: rotate({rot}deg); box-shadow: 0 14px 26px rgba(0,0,0,0.35)"><div class="kicker" style="font-size: 18px">{d}</div><div style="font-size: 25px; line-height: 1.35">{t}</div></div>'
S["Cli-05-Contenido"] = page("Primeros clientes · Contenido", "bg-sarga", "#F4F1EA", f"""
{head(3, 'DATE A CONOCER', 'Comparte <em style="font-style: italic; color: #B7CFE6">lo que sabes</em>', True, 400)}
{polaroid('oficina', 'grabando para ustedes', 720, 70, 290, 280, -4, '50% 30%', 'Berny en su oficina con micrófono')}
<p style="position: absolute; left: 80px; right: 80px; top: 480px; margin: 0; font-size: 30px; line-height: 1.45; color: rgba(244,241,234,0.88)">No necesitas ser “influencer”. Explicar lo que ves en tu día a día te posiciona como la persona que sabe.</p>
<div style="position: absolute; left: 80px; right: 80px; top: 660px; display: flex; gap: 18px">
{day('LUNES', 'Una duda que te hicieron esta semana', '#F4F1EA', '#1E242C', -2)}{day('MIÉRCOLES', 'Una fecha límite que se acerca', '#B7CFE6', '#1E242C', 1.5)}{day('VIERNES', 'Un error común y cómo evitarlo', '#D9B4A8', '#1E242C', -1)}
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1010px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#A9C9A9" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#262F3B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg><span style="font-size: 28px; line-height: 1.45">Tres temas a la semana son suficientes. <strong>Constancia le gana a perfección.</strong></span></div>
{foot('@bernardolatorre.fiscal', 5, T, True)}
""")

# 6 · Red de alianzas
def nodo(t, x, y, bg="#FFFDF8", fg="#1E242C"):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: 250px; padding: 22px 10px; background: {bg}; color: {fg}; text-align: center; font-size: 26px; font-weight: 600; border-radius: 40px; box-shadow: 0 10px 20px rgba(30,36,44,0.16)">{t}</div>'
S["Cli-06-Alianzas"] = page("Primeros clientes · Alianzas", "bg-papel", "#1E242C", f"""
{head(4, 'NO ESTÁS SOLO', 'Haz <em style="font-style: italic">alianzas</em>', False, 400)}
{polaroid('icpnl', 'mi gremio: ICPNL', 740, 60, 260, 240, 6, '30% 30%', 'Berny en el ICPNL')}
<p style="position: absolute; left: 80px; right: 380px; top: 330px; margin: 0; font-size: 30px; line-height: 1.45">Otros profesionistas ven a diario a gente que necesita un contador. Y no todos los colegas son competencia.</p>
<svg aria-hidden="true" style="position: absolute; left: 0; top: 0" width="1080" height="1350"><g stroke="#2B3542" stroke-width="3" stroke-dasharray="6 10"><path d="M540 905 L245 690"></path><path d="M540 905 L835 690"></path><path d="M540 905 L205 1110"></path><path d="M540 905 L875 1110"></path><path d="M540 905 L540 1170"></path></g></svg>
{nodo('Abogados', 120, 650)}{nodo('Administradores', 710, 650)}{nodo('Notarios', 80, 1070)}{nodo('Asesores financieros', 750, 1070, '#D6E4F2')}{nodo('Otros contadores', 415, 1150, '#CFE3C9')}
<div style="position: absolute; left: 430px; top: 860px; width: 220px; height: 90px; border-radius: 45px; background: #2B3542; color: #F4F1EA; display: flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 700; box-shadow: 0 14px 26px rgba(30,36,44,0.3)">Tú</div>
{foot('@bernardolatorre.fiscal', 6, T)}
""")

# 7 · Ruta del primer cliente
def paso(t, d, y, c):
    return (f'<div style="position: absolute; left: 80px; top: {y}px; width: 560px; display: flex; gap: 26px; align-items: flex-start">'
            f'<div style="width: 34px; height: 34px; border-radius: 50%; background: {c}; border: 5px solid #EEEAE1; flex-shrink: 0; margin-top: 4px; box-shadow: 0 0 0 2px #2B3542"></div>'
            f'<div><div class="kicker" style="font-size: 18px; color: #5F7E9E">{t}</div><div style="font-size: 28px; line-height: 1.4; margin-top: 6px">{d}</div></div></div>')
S["Cli-07-Recomienda"] = page("Primeros clientes · Que te recomienden", "bg-lino", "#1E242C", f"""
{head(5, 'TU MEJOR PUBLICIDAD', 'Que tu primer cliente <em style="font-style: italic">te recomiende</em>')}
<div aria-hidden="true" style="position: absolute; left: 99px; top: 540px; width: 3px; height: 560px; background: #2B3542"></div>
{paso('RESPONDE', 'A tiempo, aunque sea para decir “lo reviso y te aviso”.', 520, '#B7CFE6')}
{paso('EXPLICA', 'Sencillo, sin tecnicismos.', 680, '#B7CFE6')}
{paso('CUMPLE', 'Las fechas y lo que prometiste.', 810, '#A9C9A9')}
{paso('ENTREGA', 'Ordenado: acuses, cálculos y un resumen claro.', 940, '#A9C9A9')}
{polaroid('cafe', 'cliente contento = 3 más', 690, 600, 320, 300, 5, '50% 50%', 'Persona trabajando en laptop con café')}
{tape(780, 584, 140, -4, 'rgba(201,143,126,0.8)')}
{foot('@bernardolatorre.fiscal', 7, T)}
""")

# 8 · Aprende con cada cliente
S["Cli-08-Aprende"] = page("Primeros clientes · Aprende", "bg-sarga", "#F4F1EA", f"""
{head(6, 'Y NUNCA DEJES DE ESTUDIAR', 'Cada cliente <em style="font-style: italic; color: #B7CFE6">te enseña algo</em>', True, 420)}
{polaroid('foro', 'Foro Económico Fiscal', 690, 90, 330, 330, 5, '50% 60%', 'Conferencia en el Foro Económico Fiscal del ICPNL')}
<div style="position: absolute; left: 80px; top: 470px; width: 560px; display: flex; flex-direction: column; gap: 26px">
<div style="display: flex; gap: 18px; align-items: flex-start"><span class="serif" style="font-size: 50px; line-height: 1; color: #B7CFE6">→</span><span style="font-size: 29px; line-height: 1.4">Investiga y actualízate: la ley y el portal cambian cada año.</span></div>
<div style="display: flex; gap: 18px; align-items: flex-start"><span class="serif" style="font-size: 50px; line-height: 1; color: #B7CFE6">→</span><span style="font-size: 29px; line-height: 1.4">Pregunta cuando no sepas algo.</span></div>
<div style="display: flex; gap: 18px; align-items: flex-start"><span class="serif" style="font-size: 50px; line-height: 1; color: #D9B4A8">→</span><span style="font-size: 29px; line-height: 1.4">Nunca prometas algo que no puedes cumplir.</span></div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 930px; padding: 44px 48px; background: #F4F1EA; color: #1E242C; transform: rotate(-1.5deg); box-shadow: 0 18px 34px rgba(0,0,0,0.4)">
<p class="serif" style="margin: 0; font-size: 58px; line-height: 1.05; color: #2B3542">Todos los despachos empezaron <em style="font-style: italic">con un primer cliente.</em></p></div>
{foot('@bernardolatorre.fiscal', 8, T, True)}
""")

S["Cli-09-Cierre"] = cierre("¿Hacemos", "alianza?",
    "¿Eres abogado, administrador, notario o asesor? En GGTZ buscamos colegas para trabajar de la mano.",
    "Escríbeme", "<strong>¿Quieres parte 2?</strong> Comenta “PARTE 2” y te cuento cómo convertir prospectos en clientes.",
    "cerro", "50% 58%", 9, T, "Cerro de la Silla al atardecer")

for k, v in S.items():
    (HERE / f"{k}.dc.html").write_text(v)
print(len(S))
