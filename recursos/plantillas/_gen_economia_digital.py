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

# ---------- 01 Gancho: terracota liso ----------
p1 = f"""
<div class="tag" style="position:absolute;left:90px;top:110px">📲 MIÉRCOLES EN 3 LÁMINAS</div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:210px;font-size:124px;line-height:0.95">¿Adiós al <em>efectivo?</em></div>
<div class="serif" style="position:absolute;left:90px;right:90px;top:400px;font-size:60px;line-height:1.18">
A ver, siéntate.<br>
Los diputados aprobaron la Ley de Economía Digital y viene esto: <span class="hlw">los negocios tendrán que aceptar pagos digitales</span>. Tarjeta, transferencia o QR desde el celular.<br><br>
Pero ojo: el efectivo no desaparece.
</div>
<div style="position:absolute;left:90px;bottom:150px;font-size:26px;line-height:1.4;opacity:0.75">(Cámara de Diputados, 6 de octubre de 2026.<br>Ya pasó al Senado)</div>
<div style="position:absolute;right:80px;bottom:120px;transform:rotate(8deg)">{CEL}</div>
<div style="position:absolute;right:90px;top:118px;font-size:20px;letter-spacing:0.2em;font-weight:700;opacity:0.6">01 / 03</div>
"""

# ---------- 02 Detalle: marfil + recorte de hoja ----------
p2 = f"""
<div class="serif" style="position:absolute;left:90px;right:90px;top:120px;font-size:64px;line-height:1.16">
Y lo que casi nadie te dice:<br>
<span class="hl">Hacienda va a definir en qué sectores el pago digital podrá ser la única opción.</span><br>
Va a ser gradual, no de golpe.
</div>
<div style="position:absolute;left:90px;right:90px;top:540px;padding:38px 42px;background:#fff;box-shadow:0 6px 22px rgba(30,36,44,0.12);font-size:30px;line-height:1.5">
<div style="font-size:22px;color:#5F7E9E;margin-bottom:16px">Lo demás · en corto</div>
<div>• Negocios y gobierno tendrán que avisarte <span class="hl">qué formas de pago digital aceptan</span>.</div>
<div style="margin-top:12px">• Si se cae el sistema, se vale pagar en efectivo o con cheque.</div>
<div style="margin-top:12px">• Podrás abrir cuentas en línea con tu CURP digital.</div>
<div style="margin-top:12px">• Todavía no es ley: falta el Senado y que se publique en el DOF.</div>
</div>
{pie(2)}
"""

# ---------- 03 Remate: salvia + UNA foto en recorte (sin foto de Berny) ----------
FOTO = "/_blob/42d8079cc3c861ee4b89735b38496096"  # florista-mercado-celular
p3 = f"""
<div class="serif" style="position:absolute;left:90px;right:90px;top:110px;font-size:58px;line-height:1.16">
¿Y a ti en qué te pega?<br>
Si cobras en digital, <span class="hlw">cada peso queda registrado en tu banco</span>. Tu facturación y tus declaraciones tienen que cuadrar con lo que cobras.
</div>
<div style="position:absolute;left:90px;right:90px;top:530px;padding:14px 14px 0;background:#fff;box-shadow:0 6px 22px rgba(30,36,44,0.14)">
<img src="{FOTO}" alt="Florista en un mercado revisando su celular entre ramos de flores" style="display:block;width:100%;height:400px;object-fit:cover;object-position:35% 48%">
<div style="padding:12px 4px 14px;font-size:22px;color:#5F7E9E">Del puesto del mercado a la oficina: a todos nos toca.</div>
</div>
<div style="position:absolute;left:90px;right:90px;bottom:130px;font-size:30px;line-height:1.45">
Guárdalo para cuando salga en el DOF. <br>¿Dudas con tu negocio? <b style="white-space:nowrap">81 2758 0277</b>
</div>
{pie(3, "#2B3542")}
"""

(HERE / "Ecd-01.dc.html").write_text(page("Ley de Economía Digital · Gancho", "#D9B4A8", p1))
(HERE / "Ecd-02.dc.html").write_text(page("Ley de Economía Digital · Detalle", "#FFFDF8", p2))
(HERE / "Ecd-03.dc.html").write_text(page("Ley de Economía Digital · Remate", "#A9C9A9", p3))
print("ok")
