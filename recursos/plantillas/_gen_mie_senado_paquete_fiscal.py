# Miércoles en 3 láminas (28 oct 2026): el Senado aprobó el paquete fiscal 2027 (27 oct); RESICO hasta 5 millones
# avanza, pero la Ley del ISR regresa a Diputados por un cambio (excepción a armadoras y gasolineras).
# Copia de _gen_economia_digital.py (v3 aprobado): solo cambian el contenido y las 3 fotos de fondo. Prefijo Sen.
import pathlib
HERE = pathlib.Path(__file__).parent
TOT = 3

def page(title, bg, inner, h=1350):
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>{title}</title></head><body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&amp;family=Instrument+Serif:ital@0;1&amp;family=Hanken+Grotesk:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0}}
.serif{{font-family:'Archivo',sans-serif;font-weight:800;font-stretch:88%;letter-spacing:-0.03em}}
.serif em{{font-style:normal!important}}
.hl{{background:linear-gradient(transparent 12%, #B7CFE6 12%, #B7CFE6 92%, transparent 92%);padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.hlw{{background:linear-gradient(transparent 12%, #FFFDF8 12%, #FFFDF8 92%, transparent 92%);padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.tag{{font-size:22px;font-weight:700;letter-spacing:0.24em}}
</style>
</helmet>
<div style="width:1080px;height:{h}px;position:relative;overflow:hidden;background:{bg};font-family:'Hanken Grotesk',sans-serif;color:#1E242C">
{inner}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":{h}}}}}'>
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

import json, hashlib
CARRETERA, CORTE, CAFE = "4946905c29ac17fe9afde6b35b61113c", "0c01b25331aaf320141abd8e0cd57614", "15e9c1c0c5513d53a848a5eb62972dae"
SOMBRA = "text-shadow:0 2px 18px rgba(0,0,0,0.35)"

# ---------- 01 Gancho: carretera en la Huasteca (le falta un tramo al camino) ----------
p1 = f"""
{fondo(CARRETERA, '50% 30%', 'linear-gradient(180deg, rgba(20,24,30,0.88) 0%, rgba(20,24,30,0.74) 50%, rgba(20,24,30,0) 78%)')}
<div class="tag" style="position:absolute;left:90px;top:100px;color:#F4F1EA">📲 MIÉRCOLES EN 3 LÁMINAS</div>
<img src="/_blob/5b8391f45478910a1d0d8ca2823faf9b" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;right:80px;top:70px;width:120px;height:auto;transform:rotate(-8deg)">
<div class="serif" style="position:absolute;left:90px;right:230px;top:180px;font-size:96px;line-height:0.95;color:#FFFDF8;{SOMBRA}">¿Ya es oficial el RESICO de 5 millones?</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:520px;font-size:46px;line-height:1.2;color:#FFFDF8;{SOMBRA}">
El Senado aprobó el martes la reforma al ISR 2027: <span class="hl" style="color:#1E242C;text-shadow:none">el tope del RESICO sube de 3.5 a 5 millones al año</span>. Pero le hizo un cambio y regresa a Diputados.
</div>
<div style="position:absolute;left:90px;bottom:70px;padding:10px 18px;background:rgba(255,253,248,0.9);font-size:22px;line-height:1.35;color:#2B3542">Senado de la República, 27 oct 2026 · la Ley del ISR regresa a Diputados</div>
"""

# ---------- 02 Detalle: corte en la plancha + recorte de hoja ----------
p2 = f"""
{fondo(CORTE, '50% 45%', 'linear-gradient(180deg, rgba(20,24,30,0.88) 0%, rgba(20,24,30,0.62) 45%, rgba(20,24,30,0.4) 75%, rgba(20,24,30,0.85) 100%)')}
<div class="serif" style="position:absolute;left:90px;right:90px;top:110px;font-size:58px;line-height:1.16;color:#FFFDF8;{SOMBRA}">
Y lo que casi nadie te dice:<br>
el cambio del Senado <span class="hl" style="color:#1E242C;text-shadow:none">no fue en el RESICO</span>: sacó a armadoras y gasolineras del nuevo tope a deducciones.
</div>
<div style="position:absolute;left:90px;right:90px;bottom:150px;padding:34px 40px;background:#FFFDF8;box-shadow:0 10px 30px rgba(0,0,0,0.3);font-size:29px;line-height:1.45">
<div style="font-size:22px;color:#5F7E9E;margin-bottom:14px">Lo que trae el paquete</div>
<div>• Empresas en RESICO: el tope sube <span class="hl">de 35 a 50 millones</span>.</div>
<div style="margin-top:10px">• Empresas que ganan más de 50 millones: límite a sus deducciones y pérdidas.</div>
<div style="margin-top:10px">• La Ley de Ingresos 2027 ya se fue al Ejecutivo para salir en el DOF.</div>
<div style="margin-top:10px">• El ISR falta: Diputados vota el cambio y luego DOF.</div>
</div>
{pie(2, "rgba(244,241,234,0.85)")}
"""

# ---------- 03 Remate: café en la terraza ----------
p3 = f"""
{fondo(CAFE, '50% 62%', 'linear-gradient(180deg, rgba(20,24,30,0.88) 0%, rgba(20,24,30,0.7) 44%, rgba(20,24,30,0.15) 66%, rgba(20,24,30,0.82) 100%)')}
<div class="serif" style="position:absolute;left:90px;right:90px;top:110px;font-size:58px;line-height:1.16;color:#FFFDF8;{SOMBRA}">
¿Y a ti en qué te pega?<br>
Si eres persona física y facturas entre 3.5 y 5 millones al año, <span class="hl" style="color:#1E242C;text-shadow:none">en 2027 podrías entrar al RESICO</span>. Pero no cambies de régimen hasta que salga en el DOF.
</div>
<div style="position:absolute;left:90px;right:90px;bottom:130px;font-size:30px;line-height:1.45;color:#FFFDF8">
Guárdalo para cuando salga en el DOF.<br>¿Dudas con tu régimen? <b style="white-space:nowrap">81 2758 0277</b>
</div>
{pie(3, "rgba(244,241,234,0.85)")}
"""

# Versión historia (1080x1920): misma foto a todo lo alto y el contenido del post centrado
# dentro de la zona segura (nada en los 200 px de arriba ni en los 220 de abajo).
import re
def story(inner, title):
    m = re.match(r"\s*(<img[^>]*>\s*<div aria-hidden[^>]*></div>)", inner)
    bg = m.group(1); rest = inner[m.end():]
    body = bg + f'<div style="position:absolute;left:0;top:285px;width:1080px;height:1350px">{rest}</div>'
    return page(title + " · Historia", "#262F3B", body, 1920)

(HERE / "Sen-01.dc.html").write_text(page("Paquete fiscal 2027 en el Senado · Gancho", "#262F3B", p1))
(HERE / "Sen-02.dc.html").write_text(page("Paquete fiscal 2027 en el Senado · Detalle", "#262F3B", p2))
(HERE / "Sen-03.dc.html").write_text(page("Paquete fiscal 2027 en el Senado · Remate", "#262F3B", p3))
print("ok")

for n, (pp, t) in enumerate([(p1, "Gancho"), (p2, "Detalle"), (p3, "Remate")], 1):
    (HERE / f"Sen-S{n}-Story.dc.html").write_text(story(pp, "Paquete fiscal 2027 en el Senado · " + t))
print("stories ok")
