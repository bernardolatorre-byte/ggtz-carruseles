# Miércoles en 3 láminas: Ley de Economía Digital (Ecd-*), v2 con estilo "Chismesito":
# fondos lisos, texto corrido en serif, marcador, recorte de hoja blanca y garabato de línea.
# Sin fotos, sin texturas, sin foto de Berny.
import pathlib
HERE = pathlib.Path(__file__).parent
TOT = 3

def page(title, bg, inner):
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>{title}</title></head><body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=Hanken+Grotesk:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0}}
.serif{{font-family:'Instrument Serif',serif;font-weight:400}}
.hl{{background:linear-gradient(transparent 12%, #B7CFE6 12%, #B7CFE6 92%, transparent 92%);padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.hlw{{background:linear-gradient(transparent 12%, #FFFDF8 12%, #FFFDF8 92%, transparent 92%);padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.tag{{font-size:22px;font-weight:700;letter-spacing:0.24em}}
</style>
</helmet>
<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:{bg};font-family:'Hanken Grotesk',sans-serif;color:#1E242C">
{inner}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{ renderVals(){{ return {{}}; }} }}
</script></body></html>
"""

def pie(n, color="#5F7E9E"):
    return (f'<div style="position:absolute;left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;'
            f'font-size:20px;letter-spacing:0.2em;font-weight:700;color:{color}"><span>@BERNARDOLATORRE.FISCAL · GGTZ CONSULTORES</span><span>{n:02d} / {TOT:02d}</span></div>')

STROKE = 'fill="none" stroke="#1E242C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"'
CEL = (f'<svg aria-hidden="true" width="170" height="210" viewBox="0 0 80 100" {STROKE}>'
       '<rect x="18" y="6" width="44" height="86" rx="8"/><path d="M34 13h12"/>'
       '<rect x="27" y="28" width="9" height="9"/><rect x="44" y="28" width="9" height="9"/><rect x="27" y="45" width="9" height="9"/>'
       '<path d="M44 46h4M52 46v8M44 54h4"/><path d="M30 70h20"/><path d="M66 30c5 4 5 12 0 16M71 25c8 7 8 19 0 26"/></svg>')
LUPA = (f'<svg aria-hidden="true" width="170" height="170" viewBox="0 0 100 100" {STROKE}>'
        '<circle cx="42" cy="42" r="24"/><path d="M60 60l22 22"/><path d="M32 36c3-6 9-9 15-8"/></svg>')

# v3 (13 oct 2026): fotos del día a día de Berny a todo lo ancho como fondo (tendencia que pidió),
# con el texto estilo Chismesito encima (serif corrido + marcador + recorte de hoja).
def fondo(blob, pos, grad):
    return (f'<img src="/_blob/{blob}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}">'
            f'<div aria-hidden="true" style="position:absolute;inset:0;background:{grad}"></div>')

CAFE, DULCES, TACO = "15e9c1c0c5513d53a848a5eb62972dae", "459f6c4661d2af03982ad8a5f63d05bb", "55aa11df466de45299beca5fc4451c27"
SOMBRA = "text-shadow:0 2px 18px rgba(0,0,0,0.35)"

# ---------- 01 Gancho: café en la terraza ----------
p1 = f"""
{fondo(CAFE, '50% 62%', 'linear-gradient(180deg, rgba(20,24,30,0.86) 0%, rgba(20,24,30,0.7) 46%, rgba(20,24,30,0) 72%)')}
<div class="tag" style="position:absolute;left:90px;top:100px;color:#F4F1EA">📲 MIÉRCOLES EN 3 LÁMINAS</div>
<div style="position:absolute;right:90px;top:108px;font-size:20px;letter-spacing:0.2em;font-weight:700;color:rgba(244,241,234,0.7)">01 / 03</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:190px;font-size:124px;line-height:0.95;color:#FFFDF8;{SOMBRA}">¿Adiós al <em>efectivo?</em></div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:440px;font-size:52px;line-height:1.2;color:#FFFDF8;{SOMBRA}">
A ver, siéntate. Los diputados aprobaron la Ley de Economía Digital: <span class="hl" style="color:#1E242C;text-shadow:none">los negocios tendrán que aceptar pagos digitales</span>. Pero ojo: el efectivo no desaparece.
</div>
<div style="position:absolute;left:90px;bottom:70px;padding:10px 18px;background:rgba(255,253,248,0.9);font-size:22px;line-height:1.35;color:#2B3542">Cámara de Diputados, 6 oct 2026 · ya pasó al Senado</div>
"""

# ---------- 02 Detalle: puesto de dulces + recorte de hoja ----------
p2 = f"""
{fondo(DULCES, '50% 40%', 'linear-gradient(180deg, rgba(20,24,30,0.84) 0%, rgba(20,24,30,0.55) 45%, rgba(20,24,30,0.35) 75%, rgba(20,24,30,0.85) 100%)')}
<div class="serif" style="position:absolute;left:90px;right:90px;top:110px;font-size:62px;line-height:1.16;color:#FFFDF8;{SOMBRA}">
Y lo que casi nadie te dice:<br>
<span class="hl" style="color:#1E242C;text-shadow:none">Hacienda va a definir en qué sectores el pago digital podrá ser la única opción.</span> Va a ser gradual.
</div>
<div style="position:absolute;left:90px;right:90px;bottom:150px;padding:34px 40px;background:#FFFDF8;box-shadow:0 10px 30px rgba(0,0,0,0.3);font-size:29px;line-height:1.45">
<div style="font-size:22px;color:#5F7E9E;margin-bottom:14px">Lo demás · en corto</div>
<div>• Negocios y gobierno tendrán que avisarte <span class="hl">qué pagos digitales aceptan</span>.</div>
<div style="margin-top:10px">• Si se cae el sistema, se vale efectivo o cheque.</div>
<div style="margin-top:10px">• Podrás abrir cuentas en línea con tu CURP digital.</div>
<div style="margin-top:10px">• Todavía no es ley: falta el Senado y el DOF.</div>
</div>
{pie(2, "rgba(244,241,234,0.85)")}
"""

# ---------- 03 Remate: taco en la mesa ----------
p3 = f"""
{fondo(TACO, '50% 60%', 'linear-gradient(180deg, rgba(20,24,30,0.86) 0%, rgba(20,24,30,0.66) 42%, rgba(20,24,30,0.05) 66%, rgba(20,24,30,0.75) 100%)')}
<div class="serif" style="position:absolute;left:90px;right:90px;top:110px;font-size:60px;line-height:1.16;color:#FFFDF8;{SOMBRA}">
¿Y a ti en qué te pega?<br>
Si cobras en digital, <span class="hl" style="color:#1E242C;text-shadow:none">cada peso queda registrado en tu banco</span>. Tu facturación y tus declaraciones tienen que cuadrar con lo que cobras.
</div>
<div style="position:absolute;left:90px;right:90px;bottom:130px;font-size:30px;line-height:1.45;color:#FFFDF8">
Guárdalo para cuando salga en el DOF.<br>¿Dudas con tu negocio? <b style="white-space:nowrap">81 2758 0277</b>
</div>
{pie(3, "rgba(244,241,234,0.85)")}
"""

(HERE / "Ecd-01.dc.html").write_text(page("Ley de Economía Digital · Gancho", "#D9B4A8", p1))
(HERE / "Ecd-02.dc.html").write_text(page("Ley de Economía Digital · Detalle", "#FFFDF8", p2))
(HERE / "Ecd-03.dc.html").write_text(page("Ley de Economía Digital · Remate", "#A9C9A9", p3))
print("ok")
