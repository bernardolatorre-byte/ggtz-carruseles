# Genera los carruseles "5 cosas que nunca haría" (Nun-*) y "Dinero que no paga ISR" (Exe-*)
import pathlib
OUT = pathlib.Path(__file__).parent

IMG = dict(
    berny="25bcb8fe94907e94b0640cf81bd101a6",
    papel="5fe8c28b9943619ea44f604b391f1f8a", lino="6c9eecc651dcae0e49c6e32a51e1513e", sarga="dadb3c074dd971422db84d954c63babd",
    sierra="9040fcf6f15982c0e0dcbed5b75698cf", torres="57c215dc1238a66dd8701b45fb2c7983",
    pensativa="a02e797c6e63f92e4b9aa4f8ded12cb8", bolsas="1ccd1d95ade8d86a89a378fb60c1709b",
    cafe="cb53358cbd5f1694569d50016950c96f", tarjeta="91a759277f2d4e3b9a03c351430610c6",
    b500="29e4c8d2580b23552880ae35ab069428", manos="b76d35ba22dfc8f60635788e7c949071",
    familia="faddc9c76095ba578488017124a3ec07", monedas="fe5062850ea989b748a47059e0b37f26",
    llaves="2cd46b5a58bfffbfb27eeaf5ec4a9cb3", reunion="cee1524dd145415aaedc593dd9eb9df5",
    taqueria="f31af4ba04b2ab7d176e287d92455e9d", pilas="ca63cdca5b3b1bd737eae1c366d66408",
)
B = lambda k: f"/_blob/{IMG[k]}"

def page(title, cls, color, inner, bg=""):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gloock&amp;family=Instrument+Serif:ital@0;1&amp;family=Hanken+Grotesk:wght@400;500;600;700&amp;display=swap">
<style>
body{{margin:0}}
a{{color:inherit}}
.bg-lino{{background-color:#EEEAE1;background-image:url({B('lino')});background-size:cover}}
.bg-papel{{background-color:#F4F1EA;background-image:linear-gradient(rgba(95,126,158,0.10) 1px,transparent 1px),linear-gradient(90deg,rgba(95,126,158,0.10) 1px,transparent 1px),url({B('papel')});background-size:36px 36px,36px 36px,cover}}
.bg-sarga{{background-color:#262F3B;background-image:url({B('sarga')});background-size:cover}}
.hoja{{background-color:#FFFDF8;background-image:linear-gradient(rgba(255,253,248,0.62),rgba(255,253,248,0.62)),url({B('papel')});background-size:cover}}
.sticker{{filter: drop-shadow(5px 0 0 #fff) drop-shadow(-5px 0 0 #fff) drop-shadow(0 5px 0 #fff) drop-shadow(0 -5px 0 #fff) drop-shadow(0 14px 18px rgba(20,24,30,0.3))}}
.serif{{font-family:'Gloock','Instrument Serif',serif;font-weight:400}}
.serif em{{font-style:normal!important}}
.kicker{{font-size:22px;font-weight:600;letter-spacing:0.24em}}
</style>
</helmet>
<div class="{cls}" style="width: 1080px; height: 1350px; position: relative; overflow: hidden; font-family: 'Hanken Grotesk', sans-serif; color: {color};{bg}">
{inner}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"marker":{{"editor":"color","default":"#B7CFE6","options":["#B7CFE6","#A9C9A9","#D9B4A8"]}},"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{ marker: this.props.marker ?? '#B7CFE6' }};
}}
}}
</script>
</body>
</html>
"""

def foot(left, n, tot, dark=False):
    c = "rgba(244,241,234,0.6)" if dark else "#5F7E9E"
    return f'<div style="position: absolute; left: 80px; right: 80px; bottom: 60px; display: flex; justify-content: space-between; font-size: 20px; font-weight: 600; color: {c}"><span>{left}</span><span>{n:02d} / {tot:02d}</span></div>'

def polaroid(img, cap, x, y, w, h, rot, pos="50% 50%", alt=""):
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; box-sizing: border-box; padding: 12px 12px 50px; background: #FFFFFF; transform: rotate({rot}deg); box-shadow: 0 18px 34px rgba(30,36,44,0.28)">'
            f'<img src="{B(img)}" alt="{alt}" style="display: block; width: 100%; height: {h}px; object-fit: cover; object-position: {pos}">'
            f'<div style="position: absolute; left: 0; right: 0; bottom: 12px; text-align: center; font-family: \'Instrument Serif\', serif; font-style: italic; font-size: 26px; color: #2B3542">{cap}</div></div>')

def tape(x, y, w, rot, color="rgba(183,207,230,0.85)"):
    return f'<div aria-hidden="true" style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: 40px; background: {color}; transform: rotate({rot}deg)"></div>'

def num_badge(n, dark=False):
    bg = "#B7CFE6" if dark else "#2B3542"; fg = "#262F3B" if dark else "#F4F1EA"
    return f'<div class="serif" style="width: 96px; height: 96px; border-radius: 50%; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center; font-size: 64px; line-height: 1">{n}</div>'

def cierre(title, pregunta_em, texto, cta, comenta, photo=None, pos=None, n=None, tot=None, alt=None, fondo="atardecer"):
    # 13 oct 2026: sin fotos genéricas (Berny lo pidió). Fondo degradado de marca + sello + logo horizontal.
    # `photo`, `pos` y `alt` se ignoran; se conservan para no romper generadores viejos.
    import importlib.util as _u, pathlib as _p
    _s = _u.spec_from_file_location("_marca", _p.Path(__file__).parent / "_marca.py"); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
    inner = f"""
{_m.grad(fondo)}
<img src="{_m.SELLO_MARFIL}" alt="" aria-hidden="true" style="position: absolute; right: 80px; top: 80px; width: 130px; height: auto; transform: rotate(-8deg)">
<div aria-hidden="true" style="position: absolute; right: 30px; top: 790px; width: 470px; height: 470px; border-radius: 50%; background: #A9C9A9; opacity: 0.9"></div>
<img src="{B('berny')}" alt="Bernardo Latorre, Tax Consultant" style="position: absolute; right: -30px; bottom: 0; width: 540px; height: auto; filter: drop-shadow(0 14px 24px rgba(0,0,0,0.35))">
<div style="position: relative; height: 100%; box-sizing: border-box; padding: 150px 80px 64px; display: flex; flex-direction: column; gap: 30px">
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.95">{title}<br><span style="color: #B7CFE6">{pregunta_em}</span></h2>
<p style="margin: 0; max-width: 470px; font-size: 30px; line-height: 1.45; color: rgba(244,241,234,0.88)">{texto}</p>
<div style="align-self: flex-start; display: inline-flex; align-items: center; gap: 18px; padding: 26px 40px; background: #F4F1EA; color: #262F3B; font-size: 28px; font-weight: 700; border-radius: 4px">{cta}
<svg aria-hidden="true" width="30" height="20" viewBox="0 0 40 24" fill="none" stroke="#262F3B" stroke-width="2.4"><path d="M2 12h34M26 3l10 9-10 9"></path></svg></div>
<div style="max-width: 440px; padding: 22px 28px; background: rgba(244,241,234,0.08); border: 1px solid rgba(244,241,234,0.22); transform: rotate(-1.5deg); font-size: 25px; line-height: 1.4">{comenta}</div>
<div style="margin-top: auto; display: flex; flex-direction: column; gap: 8px; font-size: 24px; font-weight: 500">
<span>81 2758 0277 · @bernardolatorre.fiscal</span>
<img src="{_m.LOGO_H_MARFIL}" alt="Bernardo Latorre, Tax Consultant" style="width: 320px; height: auto; margin-left: -8px">
<span style="font-size: 15px; font-weight: 700; letter-spacing: 0.26em; color: rgba(244,241,234,0.7)">SOCIO EN GGTZ CONSULTORES</span>
</div>
</div>"""
    return page("Cierre", "", "#F4F1EA", inner, " isolation: isolate;")

def sello(text, color, rot, x, y, size=30):
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; padding: 10px 24px; border: 5px solid {color}; color: {color}; '
            f'font-size: {size}px; font-weight: 700; letter-spacing: 0.18em; border-radius: 10px; transform: rotate({rot}deg); opacity: 0.92">{text}</div>')

S = {}
# ====================== CARRUSEL A: 5 cosas que nunca haría ======================
TA = 8
S["Nun-01-Portada"] = page("Nunca haría · Portada", "bg-papel", "#1E242C", f"""
<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 300px; overflow: hidden">
<img src="{B('b500')}" alt="Billetes mexicanos de 500, 200 y 50 pesos" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%; filter: saturate(0.85)">
</div>
<svg aria-hidden="true" style="position: absolute; left: 0; top: 270px" width="1080" height="60" viewBox="0 0 1080 60" preserveAspectRatio="none"><path d="M0 0 L0 30 L40 18 L85 36 L130 14 L180 34 L230 20 L275 38 L320 16 L370 32 L420 12 L465 34 L515 22 L560 40 L610 16 L655 30 L705 14 L750 36 L800 20 L850 38 L900 18 L945 32 L995 14 L1040 30 L1080 20 L1080 0 Z" fill="none"></path><path d="M0 30 L40 18 L85 36 L130 14 L180 34 L230 20 L275 38 L320 16 L370 32 L420 12 L465 34 L515 22 L560 40 L610 16 L655 30 L705 14 L750 36 L800 20 L850 38 L900 18 L945 32 L995 14 L1040 30 L1080 20 L1080 60 L0 60 Z" fill="#F4F1EA"></path></svg>
<div style="position: absolute; left: 80px; top: 380px; right: 80px; display: flex; flex-direction: column; gap: 30px">
<div class="kicker" style="color: #5F7E9E">PALABRA DE CONTADOR</div>
<h1 class="serif" style="margin: 0; font-size: 150px; line-height: 0.86; color: #2B3542"><span style="font-size: 260px; line-height: 0.7; color: #C98F7E; float: left; margin: 18px 26px 0 -6px">5</span>cosas que <em style="font-style: italic">nunca</em> haría con mis impuestos</h1>
<p style="margin: 0; font-size: 36px; line-height: 1.35; font-weight: 500">…ni con mi dinero. <span style="background: linear-gradient(transparent 52%, #B7CFE6 52%); padding: 0 6px">La 3 casi nadie la ve venir.</span></p>
</div>
{sello('NUNCA', '#C98F7E', -12, 760, 1060, 44)}
<div style="position: absolute; left: 80px; right: 80px; bottom: 60px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600; color: #5F7E9E"><span>GGTZ Consultores · @bernardolatorre.fiscal</span><span>Desliza →</span></div>
""")

items = ["Comprar facturas", "Pedir factura de todo", "No facturar todo lo que cobro", "Revolver el dinero del negocio con el mío", "Gastar solo para “deducir”"]
rows = "".join(f'<div style="display: flex; align-items: center; gap: 30px; padding: 28px 0; border-top: 1px solid rgba(244,241,234,0.16)"><div class="serif" style="width: 64px; font-size: 70px; line-height: 1; color: #B7CFE6">{i+1}</div><div style="font-size: 34px; line-height: 1.3">{t}</div></div>' for i, t in enumerate(items))
S["Nun-02-Indice"] = page("Nunca haría · Índice", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; left: 80px; right: 80px; top: 96px; display: flex; flex-direction: column; gap: 40px">
<div class="kicker" style="color: #B7CFE6">DE LO QUE VEO EN EL DESPACHO</div>
<h2 class="serif" style="margin: 0; font-size: 84px; line-height: 0.98">Reviso leyes, cálculos y declaraciones <em style="font-style: italic; color: #B7CFE6">todos los días.</em></h2>
<p style="margin: 0; font-size: 31px; line-height: 1.45; color: rgba(244,241,234,0.85)">Por eso tengo claro lo que <strong style="color: #F4F1EA">no</strong> hago con lo mío:</p>
<div style="border-bottom: 1px solid rgba(244,241,234,0.16)">{rows}</div>
</div>
{foot('@bernardolatorre.fiscal', 2, TA, True)}
""")

S["Nun-03-Comprar"] = page("Nunca haría · Comprar facturas", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(1)}<div class="kicker" style="color: #5F7E9E">NUNCA HARÍA</div></div>
<h2 class="serif" style="margin: 0; font-size: 104px; line-height: 0.92; color: #2B3542">Comprar <em style="font-style: italic">facturas</em></h2>
<p style="margin: 0; max-width: 560px; font-size: 31px; line-height: 1.45">Facturas de operaciones que nunca pasaron, para “bajar” impuestos. Es de lo más perseguido hoy.</p>
</div>
<div style="position: absolute; left: 90px; top: 560px; width: 470px; box-sizing: border-box; padding: 40px 36px 54px; background: #FFFFFF; transform: rotate(-3deg); box-shadow: 0 20px 36px rgba(30,36,44,0.2); font-family: 'Courier New', monospace; color: #2B3542; -webkit-mask: radial-gradient(12px at 50% 100%, #0000 98%, #000) 50% / 36px 100% repeat-x">
<div style="text-align: center; font-size: 26px; font-weight: 700; letter-spacing: 0.1em">COMPROBANTE</div>
<div style="text-align: center; font-size: 18px; margin: 6px 0 24px">Servicios “de asesoría”</div>
<div style="display: flex; justify-content: space-between; font-size: 22px; padding: 6px 0"><span>Subtotal</span><span>$85,000.00</span></div>
<div style="display: flex; justify-content: space-between; font-size: 22px; padding: 6px 0"><span>IVA</span><span>$13,600.00</span></div>
<div style="display: flex; justify-content: space-between; font-size: 22px; padding: 6px 0; border-top: 2px dashed #2B3542; margin-top: 10px"><span>Comisión</span><span>8%</span></div>
<div style="text-align: center; font-size: 19px; margin-top: 24px">Operación: inexistente</div>
</div>
{sello('FALSA', '#C98F7E', -16, 210, 790, 52)}
<div style="position: absolute; right: 80px; top: 580px; width: 380px; display: flex; flex-direction: column; gap: 14px; padding: 40px 34px; background: #2B3542; color: #F4F1EA; transform: rotate(2deg); box-shadow: 0 18px 32px rgba(30,36,44,0.25)">
<div class="kicker" style="font-size: 18px; color: #D9B4A8">LO QUE TE PUEDE COSTAR</div>
<div class="serif" style="font-size: 110px; line-height: 0.9">2 a 9</div>
<div style="font-size: 30px; line-height: 1.3">años de prisión</div>
<div style="font-size: 22px; line-height: 1.4; color: rgba(244,241,234,0.75)">para quien vende <strong style="color: #F4F1EA">y para quien compra</strong> la factura.</div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 980px; font-size: 30px; line-height: 1.45">Además, el SAT publica la lista de quienes las emiten, y tus deducciones se caen con ellos. <strong>Mejor planear dentro de la ley.</strong></div>
{foot('Fuente: art. 113 Bis CFF · @bernardolatorre.fiscal', 3, TA)}
""")

S["Nun-04-Todo"] = page("Nunca haría · Factura de todo", "bg-papel", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 400px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(2)}<div class="kicker" style="color: #5F7E9E">NUNCA HARÍA</div></div>
<h2 class="serif" style="margin: 0; font-size: 96px; line-height: 0.92; color: #2B3542">Pedir factura <em style="font-style: italic">de todo</em></h2>
</div>
{polaroid('bolsas', 'el súper, la cena…', 700, 70, 300, 300, 5, '50% 60%', 'Bolsas de compras')}
{tape(800, 52, 120, -4)}
<div style="position: absolute; left: 80px; right: 80px; top: 470px; display: flex; flex-direction: column; gap: 26px">
<div class="hoja" style="position: relative; padding: 40px 44px; box-shadow: 0 12px 26px rgba(43,53,66,0.12); transform: rotate(-0.8deg)">
<div class="kicker" style="font-size: 19px; color: #C98F7E">MITO</div>
<div class="serif" style="font-size: 52px; line-height: 1.05; color: #2B3542; margin-top: 8px; text-decoration: line-through; text-decoration-color: #C98F7E; text-decoration-thickness: 4px">“Si lo facturo, lo deduzco”</div>
</div>
<div style="padding: 40px 44px; background: #2B3542; color: #F4F1EA; transform: rotate(0.6deg); box-shadow: 0 12px 26px rgba(43,53,66,0.18)">
<div class="kicker" style="font-size: 19px; color: #A9C9A9">REALIDAD</div>
<div style="font-size: 30px; line-height: 1.45; margin-top: 10px">Si eres asalariado, solo deduces gastos específicos: médicos, colegiaturas, intereses de tu casa, retiro… Una factura del súper no te regresa nada.</div>
</div>
<div style="display: flex; gap: 20px; align-items: flex-start; padding: 6px 4px"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#7FA67F" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg><span style="font-size: 29px; line-height: 1.4">Sí la pido cuando la <strong>deduzco</strong> o cuando necesito <strong>comprobar</strong> algo: el coche, una garantía, un aparato caro.</span></div>
</div>
{foot('Fuente: art. 151 LISR · @bernardolatorre.fiscal', 4, TA)}
""")

S["Nun-05-Ingresos"] = page("Nunca haría · No facturar", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(3, True)}<div class="kicker" style="color: #B7CFE6">NUNCA HARÍA</div></div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94">No facturar <em style="font-style: italic; color: #B7CFE6">todo lo que cobro</em></h2>
<p style="margin: 0; max-width: 820px; font-size: 30px; line-height: 1.45; color: rgba(244,241,234,0.85)">Además del riesgo fiscal, en papel estarías diciendo que ganas menos de lo que ganas.</p>
</div>
<div style="position: absolute; left: 80px; top: 560px; width: 560px; display: flex; flex-direction: column; gap: 18px; padding: 34px 30px; background: #E9EEF2; border-radius: 30px; box-shadow: 0 24px 46px rgba(0,0,0,0.45); transform: rotate(-2deg); color: #1E242C">
<div style="display: flex; align-items: center; gap: 14px; padding-bottom: 14px; border-bottom: 1px solid rgba(30,36,44,0.12)"><div style="width: 50px; height: 50px; border-radius: 50%; background: #5F7E9E; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 20px">BC</div><div style="font-weight: 700; font-size: 22px">Asesor de crédito</div></div>
<div style="align-self: flex-start; max-width: 420px; padding: 18px 22px; background: #FFFFFF; border-radius: 22px 22px 22px 6px; font-size: 24px; line-height: 1.35">Para tu crédito hipotecario necesito tus declaraciones de los últimos 2 años 🙂</div>
<div style="align-self: flex-end; max-width: 400px; padding: 18px 22px; background: #CFE3C9; border-radius: 22px 22px 6px 22px; font-size: 24px; line-height: 1.35">Ok… pero ahí dice que gano mucho menos 😅</div>
<div style="align-self: flex-start; max-width: 420px; padding: 18px 22px; background: #FFFFFF; border-radius: 22px 22px 22px 6px; font-size: 24px; line-height: 1.35">Con eso solo te alcanza para la mitad.</div>
</div>
{polaroid('llaves', 'la casa que no fue', 680, 600, 320, 300, 6, '50% 40%', 'Llaves con llavero de casa')}
<div style="position: absolute; left: 80px; right: 80px; top: 1060px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#D9B4A8" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#262F3B" stroke-width="2.4" stroke-linecap="round"></path></svg><span style="font-size: 28px; line-height: 1.45; color: rgba(244,241,234,0.9)">Y si gastas más de lo que declaras, el SAT puede presumir que esa diferencia es ingreso <strong style="color: #F4F1EA">(discrepancia fiscal)</strong>.</span></div>
{foot('Fuente: art. 91 LISR · @bernardolatorre.fiscal', 5, TA, True)}
""")

S["Nun-06-Revolver"] = page("Nunca haría · Revolver dinero", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(4)}<div class="kicker" style="color: #5F7E9E">NUNCA HARÍA</div></div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">Revolver el dinero del negocio <em style="font-style: italic">con el mío</em></h2>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 470px; display: grid; grid-template-columns: 1fr 1fr; gap: 26px">
<div style="display: flex; flex-direction: column; gap: 18px; padding: 40px 34px; background: #2B3542; color: #F4F1EA; transform: rotate(-1.5deg); box-shadow: 0 16px 30px rgba(43,53,66,0.2)">
<div class="kicker" style="font-size: 19px; color: #B7CFE6">CUENTA DEL NEGOCIO</div>
<div style="font-size: 27px; line-height: 1.4">Cobros a clientes</div><div style="font-size: 27px; line-height: 1.4">Proveedores y nómina</div><div style="font-size: 27px; line-height: 1.4">Impuestos</div>
<div style="margin-top: 10px; font-size: 24px; color: rgba(244,241,234,0.75)">→ Me pago un sueldo o retiro fijo</div>
</div>
<div class="hoja" style="display: flex; flex-direction: column; gap: 18px; padding: 40px 34px; transform: rotate(1.5deg); box-shadow: 0 16px 30px rgba(43,53,66,0.14)">
<div class="kicker" style="font-size: 19px; color: #7FA67F">CUENTA PERSONAL</div>
<div style="font-size: 27px; line-height: 1.4">Súper y casa</div><div style="font-size: 27px; line-height: 1.4">Salidas y viajes</div><div style="font-size: 27px; line-height: 1.4">Ahorro</div>
<div style="margin-top: 10px; font-size: 24px; color: #3A4552">← Solo recibe ese sueldo</div>
</div>
</div>
{polaroid('taqueria', 'el negocio es otro', 620, 905, 300, 230, -4, '50% 70%', 'Taquería de esquina')}
<div style="position: absolute; left: 80px; top: 920px; width: 500px; font-size: 29px; line-height: 1.45">Si todo sale de la misma cuenta, no sabes cuánto gana tu negocio <strong>ni sobre qué números</strong> estás pagando impuestos.</div>
{foot('@bernardolatorre.fiscal', 6, TA)}
""")

S["Nun-07-Deducir"] = page("Nunca haría · Gastar para deducir", "bg-papel", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(5)}<div class="kicker" style="color: #5F7E9E">NUNCA HARÍA</div></div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">Gastar solo para <em style="font-style: italic">“deducir”</em></h2>
<p style="margin: 0; max-width: 860px; font-size: 30px; line-height: 1.45">Deducir no es que te salga gratis: el gasto lo pagas completo y solo recuperas una parte.</p>
</div>
<div class="hoja" style="position: absolute; left: 80px; right: 80px; top: 520px; padding: 50px 54px; box-shadow: 0 14px 28px rgba(43,53,66,0.14); transform: rotate(-0.8deg)">
<div class="kicker" style="font-size: 20px; color: #5F7E9E">EJEMPLO, EN EL MEJOR DE LOS CASOS (TASA MÁXIMA 35%)</div>
<div style="display: grid; grid-template-columns: 1fr auto; row-gap: 22px; column-gap: 30px; margin-top: 26px; align-items: baseline">
<span style="font-size: 31px">Compras algo que no necesitas</span><span class="serif" style="font-size: 62px; color: #2B3542">$10,000</span>
<span style="font-size: 31px">Te ahorras de ISR, como máximo</span><span class="serif" style="font-size: 62px; color: #7FA67F">−$3,500</span>
<span style="font-size: 31px; font-weight: 700; padding-top: 18px; border-top: 2px solid #2B3542">Igual sale de tu bolsa</span><span class="serif" style="font-size: 80px; color: #C98F7E; padding-top: 18px; border-top: 2px solid #2B3542">$6,500</span>
</div>
</div>
{polaroid('tarjeta', '¿lo necesitaba?', 690, 980, 300, 200, 5, '50% 45%', 'Pago con tarjeta')}
<div style="position: absolute; left: 80px; top: 1010px; width: 560px; font-size: 29px; line-height: 1.45">Hay mejores formas de optimizar la carga fiscal: <strong>planear antes de gastar.</strong></div>
{foot('Fuente: art. 152 LISR · @bernardolatorre.fiscal', 7, TA)}
""")

S["Nun-08-Cierre"] = cierre("¿Con cuál", "no estás de acuerdo?",
    "Una buena decisión fiscal también tiene que ser una buena decisión financiera.",
    "Agenda tu asesoría", "<strong>Cuéntame en comentarios</strong> cuál haces tú, y guarda este post para tu próxima declaración.",
    "sierra", "50% 50%", 8, TA, "Monterrey con la Sierra Madre al fondo")

# ====================== CARRUSEL B: Dinero que no paga ISR ======================
TB = 9
S["Exe-01-Portada"] = page("No paga ISR · Portada", "", "#F4F1EA", f"""
<img src="{B('b500')}" alt="Billetes de 500 pesos" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 30% 50%; transform: scale(1.15) rotate(6deg); filter: saturate(0.7) brightness(0.55)">
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(38,47,59,0.55) 0%, rgba(38,47,59,0.2) 40%, rgba(38,47,59,0.92) 78%)"></div>
<div style="position: absolute; left: 140px; top: 150px; width: 800px; padding: 28px 30px; background: rgba(244,241,234,0.94); border-radius: 30px; color: #1E242C; display: flex; gap: 24px; align-items: center; box-shadow: 0 24px 50px rgba(0,0,0,0.4); transform: rotate(-3deg)">
<div style="width: 86px; height: 86px; border-radius: 22px; background: #2B3542; display: flex; align-items: center; justify-content: center; flex-shrink: 0"><svg aria-hidden="true" width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#B7CFE6" stroke-width="2"><path d="M3 10h18M5 10V20M10 10v10M14 10v10M19 10v10M2 21h20M12 3l9 5H3z"></path></svg></div>
<div style="display: flex; flex-direction: column; gap: 4px"><div style="display: flex; justify-content: space-between; font-size: 20px; color: #5F7E9E; font-weight: 600"><span>TU BANCO</span><span>ahora</span></div><div style="font-size: 32px; font-weight: 700">Recibiste una transferencia</div><div style="font-size: 28px">+$150,000.00 de “Papá”</div></div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 640px; display: flex; flex-direction: column; gap: 28px">
<div class="kicker" style="color: #B7CFE6">ANTES DE ENTRAR EN PÁNICO</div>
<h1 class="serif" style="margin: 0; font-size: 140px; line-height: 0.88">¿Ese dinero <em style="font-style: italic; color: #B7CFE6">paga ISR?</em></h1>
<p style="margin: 0; font-size: 34px; line-height: 1.4; font-weight: 500">5 ingresos por los que, cumpliendo requisitos, <span style="background: linear-gradient(transparent 52%, rgba(183,207,230,0.55) 52%); padding: 0 6px">no pagas impuesto</span></p>
</div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 60px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600"><span>GGTZ Consultores · @bernardolatorre.fiscal</span><span>Desliza →</span></div>
""")

def box(t, sub, bg, fg, rot):
    return f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 10px; padding: 30px 24px; background: {bg}; color: {fg}; text-align: center; transform: rotate({rot}deg); box-shadow: 0 12px 24px rgba(43,53,66,0.15)"><div class="serif" style="font-size: 44px; line-height: 1">{t}</div><div style="font-size: 22px; line-height: 1.35">{sub}</div></div>'
S["Exe-02-Regla"] = page("No paga ISR · La regla", "bg-lino", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div class="kicker" style="color: #5F7E9E">PRIMERO, LA REGLA</div>
<h2 class="serif" style="margin: 0; font-size: 92px; line-height: 0.94; color: #2B3542">Que te depositen <em style="font-style: italic">no siempre</em> es ingreso gravado</h2>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 500px; display: flex; flex-direction: column; align-items: center; gap: 0">
<div style="padding: 26px 40px; background: #2B3542; color: #F4F1EA; font-size: 32px; font-weight: 600; border-radius: 6px">Entra dinero a tu cuenta</div>
<svg aria-hidden="true" width="40" height="70" viewBox="0 0 40 70"><path d="M20 2v58M8 48l12 14 12-14" fill="none" stroke="#2B3542" stroke-width="3"></path></svg>
<div class="hoja" style="padding: 26px 40px; font-size: 32px; font-weight: 600; box-shadow: 0 10px 22px rgba(43,53,66,0.12); transform: rotate(-1deg)">¿Qué operación fue?</div>
<svg aria-hidden="true" width="760" height="80" viewBox="0 0 760 80"><path d="M380 0v20M120 20h520M120 20v56M380 20v56M640 20v56" fill="none" stroke="#2B3542" stroke-width="3"></path></svg>
<div style="display: flex; gap: 24px; width: 100%">{box('Gravado', 'Pagas ISR: sueldo, honorarios, ventas', '#D9B4A8', '#1E242C', -1.5)}{box('Exento', 'La ley lo libera, con requisitos', '#B7CFE6', '#1E242C', 1)}{box('No es ingreso', 'No es tuyo o lo tienes que devolver', '#FFFDF8', '#1E242C', -1)}</div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1100px; font-size: 29px; line-height: 1.45">La clave: <strong>poder demostrar de dónde vino.</strong></div>
{foot('Fuente: arts. 90 y 93 LISR · @bernardolatorre.fiscal', 2, TB)}
""")

def item_slide(name, n, kicker, title_html, body_html, extra, src, cls, color, dark=False):
    kc = "#B7CFE6" if dark else "#5F7E9E"
    return page(name, cls, color, f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; align-items: center; gap: 26px">{num_badge(n - 1, dark)}<div class="kicker" style="color: {kc}">{kicker}</div></div>
<h2 class="serif" style="margin: 0; font-size: 96px; line-height: 0.92; {'' if dark else 'color: #2B3542'}">{title_html}</h2>
{body_html}
</div>
{extra}
{foot(src, n + 1, TB, dark)}
""")

S["Exe-03-Prestamos"] = item_slide("No paga ISR · Préstamos", 2, "NO ES INGRESO",
    'Los <em style="font-style: italic">préstamos</em>',
    '<p style="margin: 0; max-width: 560px; font-size: 31px; line-height: 1.45">Ese dinero no es tuyo: lo tienes que devolver. Por eso no es ingreso.</p>',
    f"""{polaroid('manos', 'trato hecho… por escrito', 660, 80, 340, 330, 5, '50% 50%', 'Apretón de manos')}
{tape(760, 62, 140, -6)}
<div style="position: absolute; left: 80px; right: 80px; top: 560px; display: grid; grid-template-columns: 1fr 1fr; gap: 26px">
<div style="padding: 40px 34px; background: #2B3542; color: #F4F1EA; transform: rotate(-1deg)"><div class="kicker" style="font-size: 19px; color: #A9C9A9">NO PAGA ISR</div><div class="serif" style="font-size: 54px; line-height: 1; margin-top: 14px">El préstamo</div><div style="font-size: 25px; line-height: 1.4; margin-top: 12px; color: rgba(244,241,234,0.85)">Lo que te prestaron y vas a regresar</div></div>
<div class="hoja" style="padding: 40px 34px; transform: rotate(1deg); box-shadow: 0 12px 24px rgba(43,53,66,0.12)"><div class="kicker" style="font-size: 19px; color: #C98F7E">SÍ PAGA ISR</div><div class="serif" style="font-size: 54px; line-height: 1; margin-top: 14px; color: #2B3542">Los intereses</div><div style="font-size: 25px; line-height: 1.4; margin-top: 12px">Si tú prestas y te pagan intereses, eso sí es ingreso</div></div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1000px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#2B3542" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"></path></svg><span style="font-size: 28px; line-height: 1.45">Respáldalo con un <strong>contrato</strong> y transferencias. Si en el año pasa de <strong>$600,000</strong>, se informa en tu declaración anual.</span></div>""",
    "Fuente: art. 90 LISR · @bernardolatorre.fiscal", "bg-papel", "#1E242C")

def node(t, x, y, bg="#FFFDF8", fg="#1E242C", w=230):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; padding: 20px 10px; background: {bg}; color: {fg}; text-align: center; font-size: 27px; font-weight: 600; border-radius: 6px; box-shadow: 0 10px 20px rgba(0,0,0,0.3)">{t}</div>'
S["Exe-04-Familia"] = item_slide("No paga ISR · Donativos familia", 3, "EXENTO", 'Donativos de <em style="font-style: italic; color: #B7CFE6">tu familia directa</em>',
    '<p style="margin: 0; font-size: 30px; line-height: 1.45; color: rgba(244,241,234,0.85)">Sin límite de monto, en línea recta y entre cónyuges.</p>',
    f"""<svg aria-hidden="true" style="position: absolute; left: 0; top: 0" width="1080" height="1350"><path d="M310 590v70M310 750v70M310 910v70M425 860h120" fill="none" stroke="rgba(244,241,234,0.45)" stroke-width="3" stroke-dasharray="8 8"></path></svg>
{node('Abuelos', 195, 520)}{node('Papás', 195, 680, '#B7CFE6')}{node('Tú', 195, 820, '#F4F1EA')}{node('Cónyuge', 545, 820, '#A9C9A9')}{node('Hijos y nietos', 195, 980)}
{polaroid('familia', 'línea recta', 760, 470, 250, 260, 6, '50% 40%', 'Familia al aire libre')}
<div style="position: absolute; left: 80px; right: 80px; top: 1110px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#D9B4A8" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#262F3B" stroke-width="2.4" stroke-linecap="round"></path></svg><span style="font-size: 26px; line-height: 1.45; color: rgba(244,241,234,0.9)">Ojo: si tus papás reciben de ti, está exento siempre que no se lo donen después a otro hijo o nieto.</span></div>""",
    "Fuente: art. 93 fr. XXIII a) y b) LISR · @bernardolatorre.fiscal", "bg-sarga", "#F4F1EA", True)

S["Exe-05-Otros"] = item_slide("No paga ISR · Otros donativos", 4, "EXENTO CON TOPE", 'Donativos de <em style="font-style: italic">alguien más</em>',
    '<p style="margin: 0; max-width: 600px; font-size: 30px; line-height: 1.45">Hermanos, tíos, primos, tu pareja (si no es cónyuge), amigos…</p>',
    f"""{polaroid('monedas', 'hasta aquí', 760, 330, 240, 200, -5, '50% 50%', 'Pila de monedas')}
<div style="position: absolute; left: 80px; right: 80px; top: 610px; padding: 50px 54px; background: #2B3542; color: #F4F1EA; transform: rotate(-1deg); box-shadow: 0 18px 34px rgba(43,53,66,0.25)">
<div class="kicker" style="font-size: 20px; color: #B7CFE6">TOPE EXENTO EN 2026 (SUMA DEL AÑO)</div>
<div class="serif" style="font-size: 150px; line-height: 0.9; margin-top: 16px">$128,383</div>
<div style="font-size: 26px; color: rgba(244,241,234,0.8); margin-top: 10px">3 UMA anuales · UMA 2026: $42,794.64</div>
<div style="display: flex; height: 26px; margin-top: 34px; border-radius: 4px; overflow: hidden"><div style="flex: 0 0 64%; background: #A9C9A9"></div><div style="flex: 1; background: #D9B4A8"></div></div>
<div style="display: flex; justify-content: space-between; font-size: 22px; margin-top: 12px"><span>Hasta el tope: exento</span><span>Excedente: paga ISR</span></div>
</div>
<div style="position: absolute; left: 80px; right: 80px; top: 1120px; font-size: 29px; line-height: 1.45">Se suman todos los donativos de este tipo que recibas en el año, no uno por uno.</div>""",
    "Fuente: art. 93 fr. XXIII c) LISR; INEGI · @bernardolatorre.fiscal", "bg-lino", "#1E242C")

S["Exe-06-Herencias"] = item_slide("No paga ISR · Herencias", 5, "EXENTO", 'Herencias <em style="font-style: italic">y legados</em>',
    '<p style="margin: 0; max-width: 560px; font-size: 31px; line-height: 1.45">Lo que recibes por herencia o legado no paga ISR, sea dinero, una casa o un coche.</p>',
    f"""{polaroid('llaves', 'lo que te dejaron', 650, 380, 340, 340, 5, '50% 40%', 'Llaves con llavero de casa')}
{tape(740, 364, 150, -4, 'rgba(169,201,169,0.85)')}
<div class="hoja" style="position: absolute; left: 80px; top: 600px; width: 500px; padding: 40px 38px; box-shadow: 0 14px 28px rgba(43,53,66,0.14); transform: rotate(-2deg)">
<div class="kicker" style="font-size: 19px; color: #5F7E9E">PARA DEMOSTRARLO</div>
<div style="display: flex; flex-direction: column; gap: 18px; margin-top: 18px; font-size: 26px; line-height: 1.35">
<div style="display: flex; gap: 14px"><span style="color: #7FA67F; font-weight: 700">✓</span><span>Testamento o juicio sucesorio</span></div>
<div style="display: flex; gap: 14px"><span style="color: #7FA67F; font-weight: 700">✓</span><span>Escritura de adjudicación</span></div>
<div style="display: flex; gap: 14px"><span style="color: #7FA67F; font-weight: 700">✓</span><span>Informarlo en tu anual, si aplica</span></div>
</div></div>
<div style="position: absolute; left: 80px; right: 80px; top: 1080px; display: flex; gap: 20px; align-items: flex-start"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="#C98F7E" style="flex-shrink: 0; margin-top: 3px"><circle cx="12" cy="12" r="11"></circle><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"></path></svg><span style="font-size: 28px; line-height: 1.45">Lo que sí puede pagar ISR es cuando <strong>vendas</strong> lo que heredaste. Planéalo antes.</span></div>""",
    "Fuente: art. 93 fr. XXII LISR · @bernardolatorre.fiscal", "bg-papel", "#1E242C")

S["Exe-07-Viaticos"] = item_slide("No paga ISR · Viáticos", 6, "SI ERES ASALARIADO", 'Viáticos <em style="font-style: italic; color: #B7CFE6">comprobados</em>',
    '<p style="margin: 0; max-width: 900px; font-size: 30px; line-height: 1.45; color: rgba(244,241,234,0.85)">Lo que tu empresa te da para viajar o trabajar fuera no es sueldo, si cumples dos cosas:</p>',
    f"""<div style="position: absolute; left: 80px; right: 80px; top: 560px; display: grid; grid-template-columns: 1fr 1fr; gap: 26px">
<div style="padding: 40px 34px; background: #F4F1EA; color: #1E242C; transform: rotate(-1.5deg); box-shadow: 0 16px 30px rgba(0,0,0,0.35)"><div class="serif" style="font-size: 80px; line-height: 1; color: #5F7E9E">1</div><div style="font-size: 29px; line-height: 1.4; margin-top: 12px">Se gastan <strong>de verdad</strong> en servicio del patrón</div></div>
<div style="padding: 40px 34px; background: #B7CFE6; color: #1E242C; transform: rotate(1.5deg); box-shadow: 0 16px 30px rgba(0,0,0,0.35)"><div class="serif" style="font-size: 80px; line-height: 1; color: #2B3542">2</div><div style="font-size: 29px; line-height: 1.4; margin-top: 12px">Se comprueban con <strong>facturas (CFDI)</strong></div></div>
</div>
{polaroid('reunion', 'de viaje por trabajo', 640, 900, 320, 220, -4, '50% 60%', 'Junta de trabajo')}
<div style="position: absolute; left: 80px; top: 930px; width: 520px; font-size: 28px; line-height: 1.45; color: rgba(244,241,234,0.9)">Lo que no compruebes se puede tratar como <strong style="color: #F4F1EA">sueldo</strong> y pagar ISR.</div>""",
    "Fuente: art. 93 fr. XVII LISR · @bernardolatorre.fiscal", "bg-sarga", "#F4F1EA", True)

def postit(t, x, y, rot, bg):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: 400px; min-height: 260px; box-sizing: border-box; padding: 40px 32px; background: {bg}; transform: rotate({rot}deg); box-shadow: 0 16px 26px rgba(43,53,66,0.2); font-size: 29px; line-height: 1.4">{t}</div>'
S["Exe-08-Ojo"] = page("No paga ISR · Ojo", "bg-papel", "#1E242C", f"""
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 22px">
<div class="kicker" style="color: #5F7E9E">GUÁRDALO</div>
<h2 class="serif" style="margin: 0; font-size: 96px; line-height: 0.92; color: #2B3542">Exento <em style="font-style: italic">no es</em> “que nadie se entere”</h2>
<p style="margin: 0; font-size: 30px; line-height: 1.45">Si el SAT te pregunta, tienes que poder explicarlo:</p>
</div>
{postit('<strong>Transfiere</strong>, no en efectivo: que se vea de qué cuenta salió.', 80, 560, -4, '#FFF3B8')}
{postit('<strong>Pon por escrito</strong> préstamos y donativos (contrato o escritura, según tu estado).', 560, 540, 3, '#CFE3C9')}
{postit('<strong>Informa en tu anual</strong> préstamos, donativos y premios que sumen más de $600,000.', 100, 880, 2, '#D6E4F2')}
{postit('<strong>Guarda todo</strong>: estados de cuenta, contratos y facturas.', 580, 870, -3, '#F2D9D0')}
{foot('Fuente: art. 90 LISR · @bernardolatorre.fiscal', 8, TB)}
""")

S["Exe-09-Cierre"] = cierre("¿Te depositaron", "y no sabes qué es?",
    "Revisamos tu caso antes de tu declaración para que no pagues de más ni te lleves sustos.",
    "Agenda tu revisión", "<strong>¿Hacemos parte 2?</strong> Comenta “SÍ” y guarda este post.",
    "torres", "50% 80%", 9, TB, "Torres de Monterrey con la sierra")


# ---------- Portadas v2 (sin billetes: no repetir motivo con RESICO) ----------
def xrow(t, strike=True):
    deco = "text-decoration: line-through; text-decoration-color: #C98F7E; text-decoration-thickness: 4px;" if strike else ""
    return (f'<div style="display: flex; align-items: center; gap: 22px; padding: 20px 0; border-bottom: 2px dashed rgba(43,53,66,0.18)">'
            f'<svg aria-hidden="true" width="44" height="44" viewBox="0 0 24 24" style="flex-shrink: 0"><rect x="2" y="2" width="20" height="20" rx="4" fill="none" stroke="#2B3542" stroke-width="2"></rect><path d="M7 7l10 10M17 7L7 17" stroke="#C98F7E" stroke-width="3" stroke-linecap="round"></path></svg>'
            f'<span style="font-size: 34px; {deco}">{t}</span></div>')
S["Nun-01-Portada"] = page("Nunca haría · Portada", "", "#1E242C", f"""
<div aria-hidden="true" style="position: absolute; inset: 0; background-image: radial-gradient(rgba(43,53,66,0.13) 2px, transparent 2.5px); background-size: 30px 30px"></div>
<div class="serif" aria-hidden="true" style="position: absolute; right: -40px; top: -150px; font-size: 900px; line-height: 1; color: rgba(255,253,248,0.45)">5</div>
<div style="position: absolute; left: 80px; top: 96px; right: 80px; display: flex; flex-direction: column; gap: 26px">
<div style="align-self: flex-start; padding: 12px 22px; background: #2B3542; color: #F4F1EA; font-size: 20px; font-weight: 700; letter-spacing: 0.2em; transform: rotate(-2deg)">PALABRA DE CONTADOR</div>
<h1 class="serif" style="margin: 0; font-size: 136px; line-height: 0.88; color: #1E242C">5 cosas que <em style="font-style: italic">nunca</em> haría con mis impuestos</h1>
</div>
<div class="hoja" style="position: absolute; left: 110px; top: 700px; width: 700px; box-sizing: border-box; padding: 40px 50px 30px; transform: rotate(-3deg); box-shadow: 0 26px 50px rgba(30,36,44,0.28)">
<div class="kicker" style="font-size: 19px; color: #5F7E9E; padding-bottom: 6px">MI LISTA DE “NO”</div>
{xrow('Comprar facturas')}{xrow('Pedir factura de todo')}{xrow('No facturar todo lo que…', False)}
<div style="height: 70px; background: linear-gradient(rgba(255,253,248,0), #FFFDF8)"></div>
</div>
{tape(380, 676, 200, 4, 'rgba(255,253,248,0.75)')}
<div class="sticker" style="position: absolute; left: 720px; top: 1010px; transform: rotate(8deg)"><div style="padding: 22px 28px; background: #C98F7E; color: #FFFFFF; border-radius: 50%; width: 200px; height: 200px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; text-align: center; font-size: 25px; font-weight: 700; line-height: 1.2">La 3 casi nadie la ve venir</div></div>
<div style="position: absolute; left: 80px; right: 80px; bottom: 60px; display: flex; justify-content: space-between; font-size: 21px; font-weight: 600; color: #2B3542"><span>GGTZ Consultores · @bernardolatorre.fiscal</span><span>Desliza →</span></div>
""", bg=" background: #B7CFE6;")

S["Exe-01-Portada"] = page("No paga ISR · Portada", "bg-sarga", "#F4F1EA", f"""
<div style="position: absolute; right: 0; top: 0; width: 520px; height: 1350px; overflow: hidden">
<img src="{B('pensativa')}" alt="Mujer pensativa leyendo" style="width: 100%; height: 100%; object-fit: cover; object-position: 38% 50%">
<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(38,47,59,0.55) 0%, rgba(38,47,59,0) 30%)"></div>
</div>
<div style="position: absolute; left: 330px; top: 170px; width: 640px; padding: 26px 28px; background: rgba(244,241,234,0.96); border-radius: 30px; color: #1E242C; display: flex; gap: 22px; align-items: center; box-shadow: 0 26px 50px rgba(0,0,0,0.45); transform: rotate(-3deg)">
<div style="width: 80px; height: 80px; border-radius: 20px; background: #2B3542; display: flex; align-items: center; justify-content: center; flex-shrink: 0"><svg aria-hidden="true" width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#B7CFE6" stroke-width="2"><path d="M3 10h18M5 10V20M10 10v10M14 10v10M19 10v10M2 21h20M12 3l9 5H3z"></path></svg></div>
<div style="display: flex; flex-direction: column; gap: 4px; flex: 1"><div style="display: flex; justify-content: space-between; font-size: 19px; color: #5F7E9E; font-weight: 600"><span>TU BANCO</span><span>ahora</span></div><div style="font-size: 30px; font-weight: 700">Recibiste una transferencia</div><div style="font-size: 27px">+$150,000.00 de “Papá”</div></div>
</div>
<div style="position: absolute; left: 80px; top: 520px; width: 560px; display: flex; flex-direction: column; gap: 30px">
<div class="kicker" style="color: #B7CFE6">ANTES DE ENTRAR EN PÁNICO</div>
<h1 class="serif" style="margin: 0; font-size: 128px; line-height: 0.88">¿Ese dinero <em style="font-style: italic; color: #B7CFE6">paga ISR?</em></h1>
<p style="margin: 0; font-size: 32px; line-height: 1.4; color: rgba(244,241,234,0.9)">5 ingresos por los que, cumpliendo requisitos, <strong style="color: #F4F1EA">no pagas impuesto</strong></p>
</div>
<div style="position: absolute; left: 80px; bottom: 60px; font-size: 21px; font-weight: 600; color: rgba(244,241,234,0.8)">GGTZ Consultores · @bernardolatorre.fiscal</div>
<div style="position: absolute; right: 60px; bottom: 56px; padding: 10px 18px; background: rgba(38,47,59,0.75); font-size: 21px; font-weight: 600">Desliza →</div>
""")

for k, v in S.items():
    (OUT / f"{k}.dc.html").write_text(v)
print(len(S))
