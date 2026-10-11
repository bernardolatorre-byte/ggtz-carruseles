# Genera portadas de historias destacadas (Prf-Cov-*) y las historias que van dentro (Prf-*)
# Estilo sencillo, igual que "Chismesito fiscal": fondo liso, Instrument Serif, resaltado de marcador.
import pathlib
OUT = pathlib.Path(__file__).parent

HEAD = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Perfil</title></head><body>
<x-dc>
<helmet><style>
body{margin:0}
.serif{font-family:'Instrument Serif',serif;font-weight:400}
.k{font-size:24px;font-weight:700;letter-spacing:0.24em}
.hl{background:linear-gradient(transparent 12%, #B7CFE6 12%, #B7CFE6 92%, transparent 92%);padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.hlw{background:linear-gradient(transparent 12%, #FFFDF8 12%, #FFFDF8 92%, transparent 92%);padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.hls{background:linear-gradient(transparent 12%, #A9C9A9 12%, #A9C9A9 92%, transparent 92%);padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
</style></helmet>
"""
TAIL = """
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":1920}}'>
class Component extends DCLogic { renderVals(){ return {}; } }
</script></body></html>"""

def page(bg, inner, color="#1E242C"):
    return HEAD + f"""<div style="width:1080px;height:1920px;position:relative;overflow:hidden;background:{bg};font-family:'Hanken Grotesk',sans-serif;color:{color}">
{inner}
</div>""" + TAIL

S = 'fill="none" stroke="#262F3B" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
 "sobre-mi": f'<svg viewBox="0 0 24 24" {S}><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/></svg>',
 "servicios": f'<svg viewBox="0 0 24 24" {S}><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/></svg>',
 "empezar": f'<svg viewBox="0 0 24 24" {S}><path d="M3 21l1.65-3.8a9 9 0 1 1 3.4 2.9L3 21"/><path d="M9 12l2 2 4-4"/></svg>',
 "chismesito": f'<svg viewBox="0 0 24 24" {S}><path d="M4 10h13v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4z"/><path d="M17 12h1a2.5 2.5 0 0 1 0 5h-1"/><path d="M8 3c-1 1.3 1 2 0 3.5M11.5 3c-1 1.3 1 2 0 3.5M15 3c-1 1.3 1 2 0 3.5"/></svg>',
 "tips": f'<svg viewBox="0 0 24 24" {S}><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg>',
}
COVER_BG = {"sobre-mi":"#B7CFE6","servicios":"#A9C9A9","empezar":"#D9B4A8","chismesito":"#B7CFE6","tips":"#A9C9A9"}

# Portadas: el ícono va centrado en el círculo que recorta Instagram (centro de la historia)
for n,(name,icon) in enumerate(ICONS.items(),1):
    inner = f'<div style="position:absolute;left:340px;top:760px;width:400px;height:400px">{icon}</div>'
    (OUT/f"Prf-Cov-{n:02d}-{name}.dc.html").write_text(page(COVER_BG[name], inner))

WA = """<div style="position:absolute;left:90px;right:90px;bottom:230px;display:flex;align-items:center;gap:22px;padding:24px 32px;background:#262F3B;color:#F4F1EA;border-radius:999px">
<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#A9C9A9" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.65-3.8a9 9 0 1 1 3.4 2.9L3 21"/></svg>
<div style="flex:1"><div style="font-size:34px;font-weight:700;line-height:1.1">Escríbeme por WhatsApp</div><div style="font-size:25px;opacity:0.8;margin-top:4px">81 2758 0277 · link en mi perfil</div></div>
<div style="font-size:44px;color:#A9C9A9">→</div></div>"""
FOOT = '<div style="position:absolute;left:90px;bottom:{b}px;font-size:22px;letter-spacing:0.2em;font-weight:700;color:#5F7E9E">@BERNARDOLATORRE.FISCAL · GGTZ CONSULTORES</div>'

stories = {}
# ---- Sobre mí
stories["Prf-01-sobre-mi-1"] = page("#FFFDF8", f"""
<div class="k" style="position:absolute;left:90px;top:220px;color:#5F7E9E">SOBRE MÍ</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:300px;font-size:92px;line-height:1.05">Hola, soy <span class="hl">Bernardo</span> 👋</div>
<img src="/_blob/df12d7834689b02a85e1e7c7bb293a70" style="position:absolute;left:90px;top:560px;width:900px;height:760px;object-fit:cover;border-radius:6px">
<div class="serif" style="position:absolute;left:90px;right:90px;top:1370px;font-size:58px;line-height:1.2">Soy Contador Público y socio de GGTZ Consultores, aquí en Monterrey. Mi chamba: que tus impuestos dejen de darte miedo.</div>
""" + FOOT.format(b=240))
stories["Prf-02-sobre-mi-2"] = page("#B7CFE6", f"""
<div class="k" style="position:absolute;left:90px;top:220px">EN CORTO</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:320px;font-size:70px;line-height:1.35">
🎓 Egresado de la UDEM.<br>
🏢 <span class="hlw">8 años en Big Four:</span> 4 en Deloitte y 4 en EY.<br>
🤝 Hoy, socio en GGTZ Consultores.<br>
📚 Estudiando la Maestría en Impuestos en el IEE.<br>
🧮 Miembro activo del ICPNL.
</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:1180px;font-size:58px;line-height:1.2">Aquí te cuento lo que pasa con el SAT, sin tecnicismos.</div>
""" + FOOT.format(b=240).replace('#5F7E9E','#2B3542'))
# ---- Servicios
stories["Prf-03-servicios-1"] = page("#FFFDF8", f"""
<div class="k" style="position:absolute;left:90px;top:220px;color:#5F7E9E">EN QUÉ TE AYUDO · 1/2</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:310px;font-size:96px;line-height:1">Si eres <span class="hls">persona física</span></div>
<div style="position:absolute;left:90px;right:90px;top:600px;font-size:52px;line-height:1.75">
✔︎ Honorarios y actividad empresarial<br>
✔︎ RESICO: alta, cálculos y declaraciones<br>
✔︎ Rentas de casas o locales<br>
✔︎ Asalariados: declaración anual y devoluciones<br>
✔︎ Ponerte al corriente con el SAT
</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:1290px;font-size:58px;line-height:1.2">¿No ves tu caso? Pregúntame, seguro tiene solución.</div>
""" + WA)
stories["Prf-04-servicios-2"] = page("#A9C9A9", f"""
<div class="k" style="position:absolute;left:90px;top:220px">EN QUÉ TE AYUDO · 2/2</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:310px;font-size:96px;line-height:1">Si tienes <span class="hlw">empresa o PyME</span></div>
<div style="position:absolute;left:90px;right:90px;top:600px;font-size:52px;line-height:1.75">
✔︎ Contabilidad y declaraciones mensuales<br>
✔︎ ISR, IVA y DIOT al día<br>
✔︎ Declaración anual<br>
✔︎ Planeación fiscal para pagar lo justo<br>
✔︎ Asesoría para decisiones de negocio
</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:1290px;font-size:58px;line-height:1.2">Para que tú te enfoques en vender y no en el SAT.</div>
""" + WA)
# ---- Cómo empezar
stories["Prf-05-empezar"] = page("#D9B4A8", f"""
<div class="k" style="position:absolute;left:90px;top:220px">CÓMO EMPEZAMOS</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:300px;font-size:84px;line-height:1.05">Es más fácil de lo que crees</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:560px;font-size:62px;line-height:1.3">
<b style="font-family:'Hanken Grotesk';font-size:44px">1.</b> Me escribes por WhatsApp y me cuentas tu caso.<br><br>
<b style="font-family:'Hanken Grotesk';font-size:44px">2.</b> Platicamos y reviso <span class="hlw">en qué estás parado</span> con el SAT.<br><br>
<b style="font-family:'Hanken Grotesk';font-size:44px">3.</b> Te digo qué necesitas, cómo lo resolvemos y cuánto cuesta.
</div>
""" + WA)
# ---- Chismesito (portada de bienvenida a la sección)
stories["Prf-06-chismesito"] = page("#B7CFE6", f"""
<div class="k" style="position:absolute;left:90px;top:220px">☕ CHISMESITO FISCAL</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:420px;font-size:80px;line-height:1.18">Cada domingo te cuento <span class="hlw">la noticia fiscal de la semana</span>, como plática de café.<br><br>Aquí guardo todas. ☕</div>
<div style="position:absolute;right:90px;bottom:300px;width:220px;height:220px;transform:rotate(8deg)">{ICONS['chismesito']}</div>
""")

for k,v in stories.items():
    (OUT/f"{k}.dc.html").write_text(v)
print("ok", len(ICONS), len(stories))
