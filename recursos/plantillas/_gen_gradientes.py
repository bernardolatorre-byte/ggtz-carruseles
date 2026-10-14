# Ejemplos de fondos con degradados (mesh gradient) en la paleta de marca (Grad-*), 13 oct 2026.
# Manchas de color difuminadas + grano fino, título en Gloock y sello BL.
import pathlib
HERE = pathlib.Path(__file__).parent

def page(title, bg, blobs, inner):
    capas = "".join(
        f'<div aria-hidden="true" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:50%;background:{c};filter:blur({b}px);transform:rotate({r}deg)"></div>'
        for x, y, w, h, c, b, r in blobs)
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>{title}</title><script src="./support.js"></script></head><body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&amp;family=Hanken+Grotesk:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0}}
.serif{{font-family:'Archivo',sans-serif;font-weight:800;font-stretch:88%;letter-spacing:-0.03em}}
.tag{{font-size:22px;font-weight:700;letter-spacing:0.24em}}
</style>
</helmet>
<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:{bg};font-family:'Hanken Grotesk',sans-serif">
{capas}
<svg aria-hidden="true" width="1080" height="1350" style="position:absolute;inset:0;opacity:0.16;mix-blend-mode:overlay"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>
{inner}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{ renderVals(){{ return {{}}; }} }}
</script></body></html>
"""

SELLO_M = "/_blob/5b8391f45478910a1d0d8ca2823faf9b"
SELLO_P = "/_blob/89b150b4a0eaffd521105fa61198e074"

def sello(src, x, y, s=120, r=-8):
    return f'<img src="{src}" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:auto;transform:rotate({r}deg)">'

def pie(color):
    return f'<div style="position:absolute;left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;font-size:20px;letter-spacing:0.2em;font-weight:700;color:{color}"><span>@BERNARDOLATORRE.FISCAL</span><span>01 / 07</span></div>'

EJ = []

# 1. Neblina (como la referencia 1): pizarra arriba que se disuelve en azul polvo y marfil abajo
EJ.append(("Grad-01-Neblina", page("Degradado Neblina", "#1C2B38", [
    (-200, -150, 1200, 900, "#2D5566", 140, 0),
    (-300, 250, 1000, 700, "#152635", 120, -10),
    (300, 700, 1100, 600, "#5F8FA6", 150, 8),
    (-200, 950, 1500, 700, "#E9EEF2", 120, 0),
    (500, 1000, 700, 500, "#B7CFE6", 110, 0),
    (-100, 1050, 500, 300, "#F1E6EA", 90, 0)],
    f"""<div class="tag" style="position:absolute;left:90px;top:100px;color:rgba(244,241,234,0.85)">CIERRE FISCAL 2026</div>
{sello(SELLO_M, 880, 70)}
<div class="serif" style="position:absolute;left:90px;right:90px;top:200px;font-size:108px;line-height:1;color:#F4F1EA">Cierra el año <span style="color:#B7CFE6">sin sorpresas</span></div>
<div style="position:absolute;left:90px;right:90px;bottom:170px;font-size:34px;line-height:1.4;color:#1E242C;max-width:760px">Lo que tienes que revisar antes del 31 de diciembre, en 6 láminas.</div>
{pie('#2B3542')}""")))

# 2. Sierra al anochecer (como la referencia 2): carbón con una franja terracota y otra azul que serpentean
EJ.append(("Grad-02-Sierra", page("Degradado Sierra", "#1C2027", [
    (-350, -250, 750, 1100, "#E2B48F", 110, -18),
    (-80, -200, 700, 600, "#C98F7E", 120, 20),
    (120, -80, 900, 520, "#3E5C9A", 120, 18),
    (-330, 650, 620, 900, "#D8A784", 120, 12),
    (-100, 900, 650, 500, "#2F4A86", 120, -10)],
    f"""{sello(SELLO_M, 880, 70)}
<div class="tag" style="position:absolute;left:430px;top:600px;color:rgba(244,241,234,0.8)">RESICO 2026</div>
<div class="serif" style="position:absolute;left:430px;right:70px;top:660px;font-size:88px;line-height:1;color:#F4F1EA">¿Te conviene el <span style="color:#E2B48F">RESICO</span>?</div>
<div style="position:absolute;left:430px;right:80px;top:1010px;font-size:30px;line-height:1.45;color:rgba(244,241,234,0.82)">Quién entra, cuánto pagas y cuándo no te conviene.</div>
{pie('rgba(244,241,234,0.6)')}""")))

# 3. Salvia clara: luz suave de salvia, azul polvo y marfil, texto oscuro
EJ.append(("Grad-03-Salvia", page("Degradado Salvia", "#EEF0EA", [
    (-250, -250, 900, 800, "#A9C9A9", 130, 0),
    (500, -100, 800, 700, "#B7CFE6", 130, 0),
    (200, 600, 900, 700, "#F4F1EA", 120, 0),
    (-200, 900, 800, 600, "#CFE0CF", 120, 0),
    (650, 950, 600, 500, "#D9B4A8", 140, 0)],
    f"""<div class="tag" style="position:absolute;left:90px;top:100px;color:#2B3542">AGUINALDO</div>
{sello(SELLO_P, 880, 70)}
<div class="serif" style="position:absolute;left:90px;right:90px;top:430px;font-size:116px;line-height:1;color:#1E242C;text-align:center">Tu aguinaldo, <span style="background:linear-gradient(transparent 14%,#FFFDF8 14%,#FFFDF8 90%,transparent 90%);padding:0 10px">sin sustos</span></div>
<div style="position:absolute;left:150px;right:150px;top:740px;font-size:32px;line-height:1.45;color:#2B3542;text-align:center">Cuánto te toca, cuándo te lo pagan y qué parte no paga ISR.</div>
{pie('#2B3542')}""")))

# 4. Noche con brillo azul: pizarra profunda, un resplandor azul polvo en la esquina y un toque terracota
EJ.append(("Grad-04-Noche", page("Degradado Noche", "#151B23", [
    (450, -350, 1000, 900, "#7FA3C4", 140, 0),
    (650, -150, 600, 500, "#B7CFE6", 110, 0),
    (-300, 900, 700, 600, "#C98F7E", 160, 0),
    (-200, 300, 800, 700, "#1F2E40", 120, 0)],
    f"""<div class="tag" style="position:absolute;left:90px;top:100px;color:rgba(244,241,234,0.85)">BUZÓN TRIBUTARIO</div>
<div class="serif" style="position:absolute;left:90px;right:90px;bottom:300px;font-size:112px;line-height:1;color:#F4F1EA">Lo que el SAT <span style="color:#B7CFE6">ya sabe</span> de ti</div>
<div style="position:absolute;left:90px;right:220px;bottom:170px;font-size:30px;line-height:1.45;color:rgba(244,241,234,0.8)">Y por qué conviene que lo revises antes que él.</div>
{sello(SELLO_M, 880, 1120, 110, 6)}
<div style="position:absolute;left:90px;bottom:70px;font-size:20px;letter-spacing:0.2em;font-weight:700;color:rgba(244,241,234,0.6)">@BERNARDOLATORRE.FISCAL</div>""")))

for name, html in EJ:
    (HERE / f"{name}.dc.html").write_text(html)
print("ok")
