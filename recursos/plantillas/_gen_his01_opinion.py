# "Historias de despacho" (formato sábado): Ep. 01 — Opinión de cumplimiento negativa (His-*)
# Formato tipo publicación de X/Twitter con la voz de Berny, sobre fondos GGTZ. Historia ilustrativa.
import pathlib, re
OUT = pathlib.Path(__file__).parent
_src = (OUT / "_gen_oct20_22.py").read_text()
exec(_src.split("S = {}")[0])  # page, foot, polaroid, tape, sello, cierre, IMG, B

IMG.update(
    fabrica="e0af3e7a3af559bd05b3fb1436bcd392", andamio="8436fc96469020769a31b5247dd1a407",
    opinion="dc4a7a1dee459811d64474d9d608865d", pilas="ca63cdca5b3b1bd737eae1c366d66408",
    torres="57c215dc1238a66dd8701b45fb2c7983",
)

def post(body, dark=True, w=860, rot=0, ep="Historias de despacho · Ep. 01", x=None, y=None, glass=False):
    if glass:
        bg = "background: rgba(38,47,59,0.78); border: 1px solid rgba(244,241,234,0.18); backdrop-filter: blur(8px);"
        fg, sub, line = "#F4F1EA", "rgba(244,241,234,0.6)", "rgba(244,241,234,0.16)"
    elif dark:
        bg = "background: #1E242C;"
        fg, sub, line = "#F4F1EA", "rgba(244,241,234,0.55)", "rgba(244,241,234,0.14)"
    else:
        bg = "background: #FFFDF8;"
        fg, sub, line = "#1E242C", "#7A8796", "rgba(30,36,44,0.1)"
    pos = f"position: absolute; left: {x}px; top: {y}px;" if x is not None else "position: relative;"
    ic = sub
    return f"""<div style="{pos} width: {w}px; box-sizing: border-box; padding: 48px 50px 34px; {bg} color: {fg}; border-radius: 34px; transform: rotate({rot}deg); box-shadow: 0 30px 60px rgba(20,24,30,0.32)">
<div style="display: flex; align-items: center; gap: 20px">
<div class="serif" style="width: 84px; height: 84px; border-radius: 50%; background: #B7CFE6; color: #262F3B; display: flex; align-items: center; justify-content: center; font-size: 40px; flex-shrink: 0">BL</div>
<div style="display: flex; flex-direction: column; gap: 2px">
<div style="display: flex; align-items: center; gap: 10px; font-size: 30px; font-weight: 700">Bernardo Latorre</div>
<div style="font-size: 24px; color: {sub}">@bernardolatorre.fiscal</div></div></div>
<div style="margin-top: 30px; font-size: 36px; line-height: 1.42; display: flex; flex-direction: column; gap: 22px">{body}</div>
<div style="margin-top: 32px; padding-top: 22px; border-top: 1px solid {line}; display: flex; justify-content: space-between; align-items: center; font-size: 21px; color: {sub}">
<span>{ep}</span>
<span style="display: flex; gap: 26px">
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{ic}" stroke-width="1.8"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{ic}" stroke-width="1.8"><path d="M12 20s-7-4.4-9-8.6C1.6 8.4 3.5 5 6.8 5c2 0 3.4 1.2 5.2 3 1.8-1.8 3.2-3 5.2-3 3.3 0 5.2 3.4 3.8 6.4C19 15.6 12 20 12 20z"/></svg>
<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{ic}" stroke-width="1.8"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg>
</span></div></div>"""

def hl(t, c="#B7CFE6"):
    return f'<span style="background: linear-gradient(transparent 55%, {c} 55%); padding: 0 4px">{t}</span>'

T = 8
S = {}

S["His-01-Portada"] = page("Historias · Portada", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 92px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="align-self: flex-start; padding: 12px 22px; background: #2B3542; color: #F4F1EA; font-size: 20px; font-weight: 700; letter-spacing: 0.24em; transform: rotate(-2deg)">HISTORIAS DE DESPACHO</div>
<h1 class="serif" style="margin: 0; font-size: 118px; line-height: 0.9; color: #2B3542">Casi pierde un contrato <em style="font-style: italic; color: #5F7E9E">por $0</em></h1>
</div>
{tape(430, 512, 200, -3)}
{post('<span>Carlos casi pierde el contrato más grande de su vida. 🏗️</span><span>Y no le debía <strong>ni un peso</strong> al SAT.</span><span style="color: rgba(244,241,234,0.7)">Te cuento qué pasó 👇</span>', True, 900, -2.5, x=90, y=540)}
<div style="position: absolute; left: 80px; right: 80px; bottom: 60px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600; color: #5F7E9E"><span>GGTZ Consultores · @bernardolatorre.fiscal</span><span>Desliza →</span></div>
""")

S["His-02-Contexto"] = page("Historias · Contexto", "bg-papel", "#1E242C", f"""
{polaroid('fabrica', 'la planta que lo quería contratar', 560, 90, 420, 360, 4, '50% 50%', 'Línea de ensamble en una planta industrial')}
{tape(680, 72, 150, -5)}
<div style="position: absolute; left: 80px; top: 130px; width: 430px; display: flex; flex-direction: column; gap: 20px">
<div class="kicker" style="color: #5F7E9E">EL CONTEXTO</div>
<div class="serif" style="font-size: 76px; line-height: 0.95; color: #2B3542">Un taller, una planta y <em style="font-style: italic">un requisito</em></div>
</div>
{post(f'<span>Carlos tiene un taller de herrería en Monterrey.</span><span>Una planta industrial le ofreció un contrato de <strong>$1.2 millones</strong> para fabricar estructuras.</span><span>Antes de firmar le pidieron una sola cosa: {hl("su opinión de cumplimiento del SAT.")}</span>', False, 920, 1.5, x=80, y=560)}
{foot('Historia ilustrativa: nombre y cifras inventados', 2, T)}
""")

S["His-03-Negativa"] = page("Historias · Negativa", "bg-sarga", "#F4F1EA", f"""
{post('<span>La descargó tranquilo, sin pendientes en mente.</span><span style="font-size: 48px; line-height: 1.15" class="serif">Resultado: <em style="font-style: italic; color: #C98F7E">NEGATIVA.</em> 😶</span>', False, 820, -1.8, x=80, y=96)}
<div style="position: absolute; left: 150px; top: 650px; width: 780px; border-radius: 16px; overflow: hidden; background: #FFFFFF; transform: rotate(2deg); box-shadow: 0 26px 50px rgba(0,0,0,0.5)">
<div style="height: 48px; background: #E4E8EC; display: flex; align-items: center; gap: 10px; padding: 0 20px">
<span style="width: 14px; height: 14px; border-radius: 50%; background: #D9B4A8"></span><span style="width: 14px; height: 14px; border-radius: 50%; background: #E6D3A3"></span><span style="width: 14px; height: 14px; border-radius: 50%; background: #A9C9A9"></span>
<span style="margin-left: 16px; flex: 1; height: 28px; border-radius: 14px; background: #FFFFFF; font-size: 16px; color: #5F7E9E; display: flex; align-items: center; padding-left: 16px">sat.gob.mx · opinión del cumplimiento</span></div>
<img src="{B('opinion')}" alt="Captura del portal del SAT: servicio de opinión del cumplimiento de obligaciones fiscales" style="display: block; width: 100%; height: 400px; object-fit: cover; object-position: 50% 0%">
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1150px; font-size: 26px; line-height: 1.4; color: rgba(244,241,234,0.8)">Así se consulta en el portal del SAT. Es gratis y la puedes sacar cuando quieras.</div>
{foot('Captura: sat.gob.mx (referencia) · @bernardolatorre.fiscal', 3, T, True)}
""")

S["His-04-Siete"] = page("Historias · Siete declaraciones", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 70px; top: 40px; font-family: 'Instrument Serif', serif; font-size: 560px; line-height: 1; color: #2B3542">7</div>
<div style="position: absolute; left: 400px; top: 170px; right: 80px; display: flex; flex-direction: column; gap: 16px">
<div class="kicker" style="color: #5F7E9E">EL MOTIVO</div>
<div class="serif" style="font-size: 72px; line-height: 0.98; color: #2B3542">declaraciones mensuales <em style="font-style: italic">sin presentar</em></div>
</div>
{post(f'<span>Eran los meses en que el taller no facturó nada.</span><span>Su lógica: <strong>“si no vendí, no tengo nada que declarar”.</strong></span><span>Error común… <strong style="color: #D9B4A8">y carísimo.</strong></span>', True, 900, 2, x=90, y=690)}
{foot('@bernardolatorre.fiscal', 4, T)}
""")

S["His-05-Ley"] = page("Historias · Lo que dice la ley", "", "#F4F1EA", f"""
<img src="{B('andamio')}" alt="Trabajadores con equipo de protección en un andamio" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%">
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(38,47,59,0.35) 0%, rgba(38,47,59,0.92) 55%, rgba(38,47,59,1) 100%)"></div>
<div style="position: absolute; left: 80px; top: 90px; padding: 12px 22px; background: #B7CFE6; color: #262F3B; font-size: 20px; font-weight: 700; letter-spacing: 0.24em; transform: rotate(-2deg)">LO QUE DICE LA LEY</div>
{post(f'<span>Aunque salga <strong>en ceros</strong>, la declaración se presenta.</span><span>Si no, tu opinión sale negativa, haya o no impuesto a pagar.</span><span>También sale negativa si lo que declaras <strong style="color: #B7CFE6">no cuadra con tus facturas.</strong></span>', True, 920, -1.5, x=80, y=430, glass=True)}
{foot('Fuente: art. 32-D, fr. IV y VIII CFF · @bernardolatorre.fiscal', 5, T, True)}
""")

def opi(estado, color, rot, x, y, tachado=False):
    deco = "text-decoration: line-through; text-decoration-color: #C98F7E; text-decoration-thickness: 5px;" if tachado else ""
    return f"""<div class="hoja" style="position: absolute; left: {x}px; top: {y}px; width: 420px; height: 300px; box-sizing: border-box; padding: 36px; transform: rotate({rot}deg); box-shadow: 0 18px 34px rgba(30,36,44,0.18); display: flex; flex-direction: column; justify-content: space-between">
<div class="kicker" style="font-size: 18px; color: #5F7E9E">OPINIÓN DEL CUMPLIMIENTO</div>
<div class="serif" style="font-size: 70px; line-height: 1; color: {color}; {deco}">{estado}</div>
<div style="height: 10px; border-radius: 5px; background: rgba(95,126,158,0.18)"></div></div>"""

S["His-06-Solucion"] = page("Historias · Cómo se resolvió", "bg-papel", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 92px; right: 80px; display: flex; flex-direction: column; gap: 16px">
<div class="kicker" style="color: #5F7E9E">CÓMO SE RESOLVIÓ</div>
<div class="serif" style="font-size: 84px; line-height: 0.95; color: #2B3542">De negativa a <em style="font-style: italic">positiva</em> en días</div>
</div>
{opi('NEGATIVA', '#C98F7E', -4, 80, 330, True)}
<svg aria-hidden="true" style="position: absolute; left: 500px; top: 440px" width="90" height="60" viewBox="0 0 40 24" fill="none" stroke="#2B3542" stroke-width="2.4"><path d="M2 12h34M26 3l10 9-10 9"/></svg>
{opi('POSITIVA', '#5E8F5E', 3, 590, 340)}
{post('<span>Presentó las 7 declaraciones atrasadas (en ceros) y revisó que no quedara nada más pendiente.</span><span>Volvió a generar la opinión: <strong>positiva.</strong> Firmó el contrato. ✍️</span>', True, 920, -1, x=80, y=740)}
{foot('@bernardolatorre.fiscal', 6, T)}
""")

def postit(t, color, rot, x, y):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: 420px; height: 300px; box-sizing: border-box; padding: 34px 32px; background: {color}; color: #1E242C; transform: rotate({rot}deg); box-shadow: 0 16px 28px rgba(0,0,0,0.35); font-size: 31px; line-height: 1.38">{t}</div>'

S["His-07-Guardalo"] = page("Historias · Guárdalo", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; left: 80px; top: 92px; right: 80px; display: flex; flex-direction: column; gap: 16px">
<div class="kicker" style="color: #B7CFE6">GUÁRDALO PARA DESPUÉS</div>
<div class="serif" style="font-size: 88px; line-height: 0.95">Que no te pase <em style="font-style: italic; color: #B7CFE6">lo de Carlos</em></div>
</div>
{postit('<strong>1.</strong> Revisa tu opinión de cumplimiento <strong>cada mes</strong>, no solo cuando te la pidan.', '#B7CFE6', -3, 80, 400)}
{postit('<strong>2.</strong> Presenta tus declaraciones <strong>aunque salgan en ceros.</strong>', '#F4F1EA', 2.5, 580, 380)}
{postit('<strong>3.</strong> Que lo que declaras <strong>cuadre</strong> con las facturas que emites y recibes.', '#A9C9A9', 2, 80, 760)}
{postit('<strong>4.</strong> ¿Ya salió negativa? El documento dice qué falta: <strong>se corrige.</strong>', '#D9B4A8', -2.5, 580, 740)}
{foot('Fuente: art. 32-D CFF · @bernardolatorre.fiscal', 7, T, True)}
""")

S["His-08-Cierre"] = cierre("¿Ya revisaste", "tu opinión?",
    "Si te sale negativa, la revisamos contigo y te decimos qué falta para dejarla en positivo.",
    "Agenda tu diagnóstico",
    "💬 Comenta <strong>OPINIÓN</strong> y te digo cómo descargarla. O guárdalo para tu próximo contrato.",
    "torres", "50% 55%", T, T, "Torres de Monterrey con la sierra al fondo")

for k, v in S.items():
    (OUT / f"{k}.dc.html").write_text(v)
print(len(S))
