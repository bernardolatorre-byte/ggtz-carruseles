# Carrusel "Buen Fin 2026" (Bfin-*), programado para martes 10 nov 2026
import importlib.util, pathlib, io, contextlib
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("base", HERE / "_gen_oct20_22.py")
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)
page, foot, polaroid, tape, cierre, sello, num_badge = base.page, base.foot, base.polaroid, base.tape, base.cierre, base.sello, base.num_badge
base.IMG.update(carritoosc="dd6f80d3e9a164f540c89581b6ef0337", tv="0341e1000fe28e333061b1328b83e2b1",
                mall="3110b2461179542afeae0468e90f0970", ebf="e933984a0f932c680adec5c2f1add845",
                sierra="9040fcf6f15982c0e0dcbed5b75698cf")
B = base.B
T = 8
S = {}

def check(t, done=True):
    box = ('<svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" style="flex-shrink: 0; margin-top: 2px"><rect x="2" y="2" width="20" height="20" rx="4" fill="#FFFDF8" stroke="#2B3542" stroke-width="2"></rect>'
           + ('<path d="M6.5 12.5l3.5 3.5L17.5 8" fill="none" stroke="#7FA67F" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path>' if done else '') + '</svg>')
    return f'<div style="display: flex; gap: 20px; align-items: flex-start; padding: 18px 0; border-bottom: 2px dashed rgba(43,53,66,0.15)">{box}<span style="font-size: 28px; line-height: 1.4">{t}</span></div>'

# 1 · Portada: foto oscura del carrito + etiqueta colgante terracota
S["Bfin-01-Portada"] = page("Buen Fin · Portada", "", "#F4F1EA", f"""
<img src="{B('carritoosc')}" alt="Carrito de súper bajo una lámpara" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 70%">
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(38,47,59,0.85) 0%, rgba(38,47,59,0.35) 45%, rgba(38,47,59,0.1) 70%, rgba(38,47,59,0.6) 100%)"></div>
<div style="position: absolute; left: 80px; right: 80px; top: 90px; display: flex; flex-direction: column; gap: 26px">
<div class="kicker" style="color: #B7CFE6">ANTES DE LLENAR EL CARRITO</div>
<h1 class="serif" style="margin: 0; font-size: 140px; line-height: 0.88">Buen Fin <em style="font-style: italic; color: #B7CFE6">sin arrepentirte</em></h1>
<p style="margin: 0; max-width: 640px; font-size: 32px; line-height: 1.4; color: rgba(244,241,234,0.9)">Facturas, sorteo del SAT, meses sin intereses y lo que debe saber tu negocio.</p>
</div>
<svg aria-hidden="true" style="position: absolute; left: 0; top: 0" width="1080" height="1350"><path d="M890 560 C 900 640, 850 700, 840 760" fill="none" stroke="#F4F1EA" stroke-width="4"></path></svg>
<div style="position: absolute; left: 640px; top: 740px; width: 340px; transform: rotate(-12deg); filter: drop-shadow(0 22px 30px rgba(0,0,0,0.45))">
<svg aria-hidden="true" width="340" height="400" viewBox="0 0 340 400" style="position: absolute; left: 0; top: 0"><path d="M100 0 H240 L340 90 V380 Q340 400 320 400 H20 Q0 400 0 380 V90 Z" fill="#C98F7E"></path><circle cx="170" cy="70" r="20" fill="#262F3B"></circle></svg>
<div style="position: relative; height: 400px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding-top: 70px; color: #FFFDF8; text-align: center">
<div class="kicker" style="font-size: 20px">2026</div>
<div class="serif" style="font-size: 92px; line-height: 0.9">13–17</div>
<div style="font-size: 30px; font-weight: 700; letter-spacing: 0.2em">NOVIEMBRE</div>
</div></div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 50px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600; color: rgba(244,241,234,0.85)"><span>GGTZ Consultores · @bernardolatorre.fiscal</span><span>Desliza →</span></div>
""")

# 2 · Fechas + captura del sitio oficial en celular
days = [("VIE", "13"), ("SÁB", "14"), ("DOM", "15"), ("LUN", "16"), ("MAR", "17")]
dhtml = "".join(f'<div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 18px 0 14px; background: {"#2B3542" if i in (0, 4) else "#FFFDF8"}; color: {"#F4F1EA" if i in (0, 4) else "#2B3542"}; border-radius: 8px; box-shadow: 0 8px 16px rgba(43,53,66,0.12)"><div class="kicker" style="font-size: 16px">{d}</div><div class="serif" style="font-size: 62px; line-height: 1">{n}</div></div>' for i, (d, n) in enumerate(days))
S["Bfin-02-Fechas"] = page("Buen Fin · Fechas", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; width: 540px; display: flex; flex-direction: column; gap: 22px">
<div class="kicker" style="color: #5F7E9E">ES OFICIAL</div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">5 días de <em style="font-style: italic">ofertas</em></h2>
<p style="margin: 0; font-size: 29px; line-height: 1.45">Este año empieza en viernes y termina en martes. Lo coordina la Secretaría de Economía.</p>
</div>
<div style="position: absolute; right: 70px; top: 90px; width: 330px; height: 620px; box-sizing: border-box; padding: 12px; background: #12161C; border-radius: 48px; transform: rotate(5deg); box-shadow: 0 30px 56px rgba(30,36,44,0.45)">
<div style="width: 100%; height: 100%; border-radius: 38px; overflow: hidden; background: #FFFFFF"><img src="{B('ebf')}" alt="Sitio oficial de El Buen Fin 2026 en celular" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 0"></div></div>
<div style="position: absolute; left: 80px; right: 80px; top: 800px; display: flex; gap: 14px">{dhtml}</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1010px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#2B3542" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"></path></svg><span style="font-size: 28px; line-height: 1.45">Revisa que la tienda sea participante en el buscador oficial: <strong>elbuenfin.org</strong></span></div>
{foot('Fuente y captura: elbuenfin.org · @bernardolatorre.fiscal', 2, T)}
""")

# 3 · Sorteo del SAT: tarjeta dibujada
S["Bfin-03-Sorteo"] = page("Buen Fin · Sorteo", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(1, True)}<div class="kicker" style="color: #B7CFE6">SORTEO EL BUEN FIN</div></div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94">Paga con tarjeta <em style="font-style: italic; color: #B7CFE6">y participa</em></h2>
</div>
<div style="position: absolute; left: 90px; top: 430px; width: 500px; height: 310px; border-radius: 26px; background: linear-gradient(135deg, #B7CFE6 0%, #5F7E9E 100%); transform: rotate(-6deg); box-shadow: 0 30px 50px rgba(0,0,0,0.5); color: #1E242C">
<div style="position: absolute; left: 40px; top: 40px; width: 70px; height: 54px; border-radius: 10px; background: #E7D9A8"></div>
<div style="position: absolute; left: 40px; top: 150px; font-family: 'Courier New', monospace; font-size: 30px; letter-spacing: 0.08em; white-space: nowrap">•••• •••• •••• 2026</div>
<div style="position: absolute; left: 40px; bottom: 36px; font-size: 20px; font-weight: 700; letter-spacing: 0.16em">CRÉDITO O DÉBITO</div>
</div>
<div style="position: absolute; right: 70px; top: 540px; width: 320px; padding: 34px 30px; background: #F4F1EA; color: #1E242C; transform: rotate(3deg); box-shadow: 0 18px 30px rgba(0,0,0,0.4)">
<div class="kicker" style="font-size: 17px; color: #5F7E9E">BOLSA DE PREMIOS HASTA</div>
<div class="serif" style="font-size: 84px; line-height: 0.95; color: #2B3542; margin-top: 8px">$500 M</div>
<div style="font-size: 21px; line-height: 1.4; margin-top: 8px">entre compradores y comercios</div></div>
<div style="position: absolute; left: 80px; right: 80px; top: 870px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; gap: 18px"><span class="serif" style="font-size: 44px; line-height: 1; color: #B7CFE6">→</span><span style="font-size: 29px; line-height: 1.4">Compras de <strong>$250 o más</strong>, del 13 al 17 de noviembre</span></div>
<div style="display: flex; gap: 18px"><span class="serif" style="font-size: 44px; line-height: 1; color: #B7CFE6">→</span><span style="font-size: 29px; line-height: 1.4">Con <strong>tarjeta de crédito o débito</strong>, en comercios participantes</span></div>
<div style="display: flex; gap: 18px"><span class="serif" style="font-size: 44px; line-height: 1; color: #D9B4A8">→</span><span style="font-size: 29px; line-height: 1.4">En efectivo <strong>no participas</strong></span></div>
</div>
{foot('Fuente: Decreto DOF 30/09/2026; elbuenfin.org · @bernardolatorre.fiscal', 3, T, True)}
""")

# 4 · Compras para tu negocio: factura + bancarizado
S["Bfin-04-Factura"] = page("Buen Fin · Factura", "bg-papel", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 400px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(2)}<div class="kicker" style="color: #5F7E9E">SI COMPRAS PARA TU NEGOCIO</div></div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">Pide tu <em style="font-style: italic">factura</em> bien hecha</h2>
</div>
{polaroid('tv', 'la pantalla de la sala de juntas', 700, 80, 300, 300, 5, '50% 45%', 'Pantalla grande en una sala')}
<div class="hoja" style="position: absolute; left: 80px; right: 80px; top: 500px; padding: 40px 46px; box-shadow: 0 14px 28px rgba(43,53,66,0.14); transform: rotate(-0.8deg)">
<div class="kicker" style="font-size: 19px; color: #5F7E9E">QUE TU CFDI TRAIGA</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 30px; margin-top: 10px">
{check('Tu RFC y nombre exactos')}{check('Tu régimen fiscal')}{check('Tu código postal fiscal')}{check('El uso de CFDI correcto')}
</div></div>
<div style="position: absolute; left: 80px; right: 80px; top: 950px; padding: 36px 40px; background: #2B3542; color: #F4F1EA; transform: rotate(0.8deg)">
<div style="display: flex; gap: 26px; align-items: center"><div class="serif" style="font-size: 84px; line-height: 1; color: #B7CFE6">$2,000</div>
<div style="font-size: 27px; line-height: 1.4">Si pasa de esto, págalo con <strong>tarjeta o transferencia</strong>. En efectivo no lo puedes deducir.</div></div></div>
{foot('Fuente: art. 27 fr. III LISR · @bernardolatorre.fiscal', 4, T)}
""")

# 5 · Meses sin intereses: 12 bloques
blocks = "".join(f'<div style="height: 120px; border-radius: 8px; background: {"#2B3542" if i < 3 else "rgba(43,53,66,0.18)"}; color: {"#F4F1EA" if i < 3 else "#2B3542"}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px"><div class="kicker" style="font-size: 14px">MES {i+1}</div><div class="serif" style="font-size: 34px">$1,000</div></div>' for i in range(12))
S["Bfin-05-MSI"] = page("Buen Fin · MSI", "", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(3)}<div class="kicker" style="color: #2B3542">TU BOLSILLO TAMBIÉN CUENTA</div></div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #1E242C">Meses sin intereses <em style="font-style: italic">no es gratis</em></h2>
<p style="margin: 0; max-width: 880px; font-size: 30px; line-height: 1.45">Es dinero de tus próximos meses. Antes de dividir, suma.</p>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 560px; padding: 36px 36px 30px; background: #FFFDF8; box-shadow: 0 16px 30px rgba(43,53,66,0.16); transform: rotate(-0.8deg)">
<div style="display: flex; justify-content: space-between; align-items: baseline"><div class="kicker" style="font-size: 18px; color: #5F7E9E">EJEMPLO</div><div style="font-size: 26px"><strong>$12,000</strong> a 12 MSI</div></div>
<div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-top: 22px">{blocks}</div>
<div style="font-size: 25px; line-height: 1.4; margin-top: 20px; color: #3A4552">Un año entero pagando $1,000 al mes. ¿Ya tenías otras mensualidades?</div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1080px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#2B3542" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#A9C9A9" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg><span style="font-size: 28px; line-height: 1.45">Regla sana: que tus mensualidades no rebasen lo que puedes pagar <strong>sin tocar tus gastos fijos</strong>.</span></div>
{foot('@bernardolatorre.fiscal', 5, T)}
""", bg=" background: #A9C9A9;")

# 6 · Si vendes en Buen Fin
S["Bfin-06-Vendes"] = page("Buen Fin · Si vendes", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 400px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(4, True)}<div class="kicker" style="color: #B7CFE6">SI TU NEGOCIO VENDE</div></div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94">El descuento <em style="font-style: italic; color: #B7CFE6">también se factura</em></h2>
</div>
{polaroid('mall', 'temporada alta', 710, 90, 290, 300, 5, '50% 30%', 'Centro comercial con gente')}
<div style="position: absolute; left: 80px; top: 520px; width: 560px; box-sizing: border-box; padding: 34px 34px 40px; background: #FFFFFF; color: #2B3542; transform: rotate(-2deg); box-shadow: 0 20px 36px rgba(0,0,0,0.45); font-family: 'Courier New', monospace">
<div style="text-align: center; font-size: 24px; font-weight: 700; letter-spacing: 0.1em">CFDI 4.0</div>
<div style="display: flex; justify-content: space-between; font-size: 23px; padding: 10px 0; margin-top: 14px"><span>Importe</span><span>$10,000.00</span></div>
<div style="display: flex; justify-content: space-between; font-size: 23px; padding: 10px 0; color: #C98F7E"><span>Descuento</span><span>−$3,000.00</span></div>
<div style="display: flex; justify-content: space-between; font-size: 23px; padding: 10px 0; border-top: 2px dashed #2B3542"><span>Base IVA</span><span>$7,000.00</span></div>
<div style="display: flex; justify-content: space-between; font-size: 23px; padding: 10px 0"><span>IVA 16%</span><span>$1,120.00</span></div>
<div style="display: flex; justify-content: space-between; font-size: 25px; font-weight: 700; padding: 10px 0; border-top: 2px solid #2B3542"><span>Total</span><span>$8,120.00</span></div>
</div>
<div style="position: absolute; left: 690px; right: 80px; top: 560px; display: flex; flex-direction: column; gap: 26px">
<div style="font-size: 27px; line-height: 1.4">El descuento va <strong>en su campo</strong> del CFDI, y el IVA se calcula <strong>sobre el precio rebajado</strong>.</div>
<div style="font-size: 27px; line-height: 1.4">Factura <strong>todas</strong> las ventas, con o sin oferta.</div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1080px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#B7CFE6" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#262F3B" stroke-width="2.4" stroke-linecap="round"></path></svg><span style="font-size: 27px; line-height: 1.45; color: rgba(244,241,234,0.9)">¿Quieres entrar? El registro es gratis en elbuenfin.org y para comercios hay <strong style="color: #F4F1EA">$100 millones</strong> en premios del SAT.</span></div>
{foot('Fuente: elbuenfin.org · @bernardolatorre.fiscal', 6, T, True)}
""")

# 7 · Checklist antes de comprar
S["Bfin-07-Checklist"] = page("Buen Fin · Checklist", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 18px">
<div class="kicker" style="color: #5F7E9E">GUÁRDALO PARA EL 13 DE NOVIEMBRE</div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">Tu lista <em style="font-style: italic">antes de comprar</em></h2>
</div>
<div class="hoja" style="position: absolute; left: 110px; right: 110px; top: 400px; padding: 46px 54px 30px; box-shadow: 0 18px 34px rgba(43,53,66,0.16); transform: rotate(-1.2deg)">
{check('Compara precios desde antes en <strong>“Quién es Quién en los Precios”</strong> de Profeco.')}
{check('Compra en la tienda oficial o en sitios seguros (cuidado con las páginas falsas).')}
{check('Paga con tarjeta si quieres entrar al sorteo.')}
{check('Pide tu factura en el momento o guarda el ticket.')}
{check('Suma tus mensualidades antes de usar MSI.', False)}
</div>
{tape(420, 380, 220, 3, 'rgba(201,143,126,0.8)')}
{foot('@bernardolatorre.fiscal', 7, T)}
""")

S["Bfin-08-Cierre"] = cierre("¿Vas a comprar para", "tu negocio?",
    "Te ayudo a que tus facturas sí cuenten y a planear tus compras de fin de año.",
    "Agenda tu asesoría", "<strong>Guárdalo</strong> y compártelo con quien ya está haciendo su lista del Buen Fin.",
    "sierra", "50% 50%", 8, T, "Monterrey con la Sierra Madre")

for k, v in S.items():
    (HERE / f"{k}.dc.html").write_text(v)
print(len(S))
