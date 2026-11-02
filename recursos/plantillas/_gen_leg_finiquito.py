# Lunes legal #3 (2 nov 2026): "¿Finiquito o liquidación?" (Leg3-*).
# Fuente: Ley Federal del Trabajo, verificada en Luthor (corte 31 oct 2026):
# arts. 33, 47, 48, 50, 53, 76, 79, 80, 87 y 162 LFT.
import importlib.util as _u, pathlib
HERE = pathlib.Path(__file__).parent
def _load(n):
    s = _u.spec_from_file_location(n, HERE / f"{n}.py"); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
G = _load("_gen_oct20_22"); M = _load("_marca")
page, foot, cierre, sello = G.page, G.foot, G.cierre, G.sello
TOT = 7
H = "@bernardolatorre.fiscal"
G.IMG["andamio"] = "8436fc96469020769a31b5247dd1a407"; ANDAMIO = "andamio"
INK = "#1E242C"
PIZ = "#2B3542"
MK = lambda c: f"background:linear-gradient(transparent 14%,{c} 14%,{c} 92%,transparent 92%);padding:0 10px"
S = []

# 1. Portada (degradado salvia): dos sobres de pago, uno delgado y uno gordo (motivo: sobres)
def sobre(x, y, w, h, rot, bg, label, sub, grosor, z):
    capas = "".join(
        f'<div style="position:absolute;left:{6*i}px;top:{-6*i}px;width:{w}px;height:{h}px;background:{bg};filter:brightness({1-0.05*i});border-radius:6px;box-shadow:0 4px 8px rgba(30,36,44,0.12)"></div>'
        for i in range(grosor, 0, -1))
    return f"""
<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);z-index:{z}">
  {capas}
  <div style="position:absolute;inset:0;background:{bg};border-radius:6px;box-shadow:0 22px 40px rgba(30,36,44,0.25);overflow:hidden">
    <svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;inset:0">
      <path d="M0 0 L{w/2} {h*0.48} L{w} 0" fill="none" stroke="rgba(30,36,44,0.28)" stroke-width="3"/>
      <path d="M0 {h} L{w*0.38} {h*0.42} M{w} {h} L{w*0.62} {h*0.42}" fill="none" stroke="rgba(30,36,44,0.12)" stroke-width="2"/>
    </svg>
    <div style="position:absolute;left:28px;right:28px;bottom:26px;padding:16px 20px;background:#FFFDF8;border:2px solid {PIZ};border-radius:4px">
      <div style="font-size:16px;font-weight:700;letter-spacing:0.24em;color:#5F7E9E">{sub}</div>
      <div class="serif" style="font-size:44px;line-height:1;margin-top:6px;color:{PIZ}">{label}</div>
    </div>
  </div>
</div>"""
S.append(("Leg3-01-Portada", page("Lunes legal: finiquito o liquidación", "", INK, f"""
{M.grad("salvia")}
<img src="{M.SELLO_PIZARRA}" alt="Sello BL, Bernardo Latorre Tax Consultant" style="position:absolute;left:84px;top:84px;width:118px;transform:rotate(-8deg)">
<div class="kicker" style="position:absolute;right:90px;top:120px;font-weight:700;color:{PIZ}">⚖️ LUNES LEGAL</div>
{sobre(110, 250, 400, 270, -6, "#FFFDF8", "Finiquito", "LO QUE YA GANÓ", 1, 2)}
{sobre(560, 230, 420, 290, 5, "#D9B4A8", "Liquidación", "FINIQUITO + INDEMNIZACIÓN", 7, 1)}
{G.tape(230, 236, 130, -10)}
<h1 class="serif" style="position:absolute;left:90px;right:90px;top:660px;margin:0;font-size:138px;line-height:0.92;color:{PIZ}">¿Finiquito o <span style="{MK('#D9B4A8')}">liquidación?</span></h1>
<p style="position:absolute;left:90px;width:760px;top:1000px;margin:0;font-size:34px;line-height:1.4;color:{PIZ}">No son lo mismo, y confundirlos le sale caro a tu empresa. Lo que dice la ley, sin rodeos.</p>
<div style="position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;font-size:21px;font-weight:600;color:{PIZ}"><span>GGTZ Consultores · {H}</span><span>Desliza →</span></div>
""", " isolation: isolate;")))

# 2. Quiz (lino) + polaroid
ops = [("A", "Sí: 3 meses de salario y 20 días por año."), ("B", "No: le toca su finiquito."), ("C", "Nada: ella fue la que se fue.")]
oo = "".join(
    f'<div style="display:flex;gap:24px;align-items:center;padding:24px 28px;background:#FFFDF8;border:2px solid {PIZ};border-radius:10px;transform:rotate({r}deg);box-shadow:0 10px 20px rgba(30,36,44,0.12)">'
    f'<div class="serif" style="flex:none;width:68px;height:68px;border-radius:50%;background:{bg};display:flex;align-items:center;justify-content:center;font-size:40px;line-height:1;color:{PIZ}">{l}</div>'
    f'<div style="font-size:31px;line-height:1.3;font-weight:600;color:{PIZ}">{t}</div></div>'
    for (l, t), r, bg in zip(ops, [-0.8, 0.6, -0.4], ["#B7CFE6", "#A9C9A9", "#D9B4A8"]))
S.append(("Leg3-02-Quiz", page("Pregunta rápida", "bg-lino", INK, f"""
<div style="position:absolute;left:90px;top:110px;width:540px">
<div class="kicker" style="color:#5F7E9E;font-weight:700">PREGUNTA RÁPIDA</div>
<h2 class="serif" style="margin:24px 0 0;font-size:72px;line-height:0.98;color:{PIZ}">Tu empleada renuncia después de 2 años. ¿Le debes <span style="{MK('#B7CFE6')}">liquidación?</span></h2>
</div>
{G.polaroid(ANDAMIO, "", 690, 120, 300, 360, 5, "50% 40%", "Dos trabajadores de espaldas con equipo de protección en un andamio")}
{G.tape(790, 104, 120, -6)}
<div style="position:absolute;left:90px;right:90px;top:640px;display:flex;flex-direction:column;gap:26px">{oo}</div>
<div style="position:absolute;left:90px;right:90px;top:1110px;font-size:28px;font-weight:600;color:{PIZ}">Piénsalo antes de deslizar. La respuesta, en la siguiente →</div>
{foot("Fuente: arts. 53 y 162 LFT · " + H, 2, TOT)}""")))

# 3. Respuesta: finiquito (degradado noche) + recibo
def fila(t, art):
    return (f'<div style="display:flex;justify-content:space-between;gap:20px;align-items:baseline;padding:20px 0;border-bottom:2px dashed rgba(43,53,66,0.25)">'
            f'<div style="font-size:29px;line-height:1.3;color:{INK}">{t}</div><div style="flex:none;font-size:20px;font-weight:700;color:#5F7E9E">{art}</div></div>')
recibo = (fila("Días trabajados que no se le han pagado", "") +
          fila("Aguinaldo proporcional (15 días al año, mínimo)", "art. 87") +
          fila("Vacaciones pendientes o proporcionales", "arts. 76 y 79") +
          fila("Prima vacacional (25% mínimo)", "art. 80") +
          fila("Prima de antigüedad: 12 días por año, <b>solo si cumplió 15 años</b>", "art. 162"))
S.append(("Leg3-03-Finiquito", page("Respuesta: finiquito", "", "#F4F1EA", f"""
{M.grad("noche")}
<div style="position:absolute;left:90px;right:90px;top:100px">
<div class="kicker" style="color:#A9C9A9;font-weight:700">RESPUESTA: B</div>
<h2 class="serif" style="margin:22px 0 18px;font-size:92px;line-height:0.95">Le toca su <span style="background:#B7CFE6;color:{INK};padding:0 12px">finiquito</span></h2>
<p style="margin:0;width:620px;font-size:31px;line-height:1.42;color:rgba(244,241,234,0.92);text-shadow:0 2px 12px rgba(10,14,20,0.6)">El finiquito es lo que la persona <b style="color:#F4F1EA">ya se ganó</b>. Se paga siempre, termine como termine la relación: renuncia, despido o fin de contrato.</p>
</div>
<div style="position:absolute;left:110px;right:110px;top:520px;padding:40px 46px 40px;background:#FFFDF8;transform:rotate(-1deg);box-shadow:0 24px 40px rgba(0,0,0,0.35);clip-path:polygon(0 0,100% 0,100% 100%,96% 98.5%,92% 100%,88% 98.5%,84% 100%,80% 98.5%,76% 100%,72% 98.5%,68% 100%,64% 98.5%,60% 100%,56% 98.5%,52% 100%,48% 98.5%,44% 100%,40% 98.5%,36% 100%,32% 98.5%,28% 100%,24% 98.5%,20% 100%,16% 98.5%,12% 100%,8% 98.5%,4% 100%,0 98.5%)">
<div style="display:flex;justify-content:space-between;align-items:baseline"><div class="serif" style="font-size:44px;color:{PIZ}">FINIQUITO</div><div style="font-size:18px;font-weight:700;letter-spacing:0.24em;color:#C98F7E">LO MÍNIMO</div></div>
{recibo}
<div style="font-size:22px;line-height:1.4;margin-top:16px;color:#3A4552">Más lo que haya pendiente: horas extra, comisiones, bonos pactados.</div>
</div>
{foot("Fuente: arts. 76, 79, 80, 87 y 162 LFT · " + H, 3, TOT, True)}""", " isolation: isolate;")))

# 4. Liquidación (terracota liso) con "3" gigante y fórmula en bloques
def bloque(t, sub, bg, fg, rot):
    return (f'<div style="flex:1;padding:34px 20px;background:{bg};color:{fg};border-radius:8px;transform:rotate({rot}deg);box-shadow:0 12px 22px rgba(30,36,44,0.16);text-align:center">'
            f'<div class="serif" style="font-size:46px;line-height:1">{t}</div><div style="font-size:22px;line-height:1.3;margin-top:8px">{sub}</div></div>')
mas = f'<div class="serif" style="flex:none;font-size:56px;color:{PIZ}">+</div>'
S.append(("Leg3-04-Liquidacion", page("Liquidación", "", INK, f"""
<div class="serif" aria-hidden="true" style="position:absolute;right:-30px;top:-170px;font-size:820px;line-height:1;color:rgba(255,253,248,0.30)">3</div>
<div style="position:absolute;left:90px;right:90px;top:130px">
<div class="kicker" style="color:{PIZ};font-weight:700">CUANDO DESPIDES SIN CAUSA</div>
<h2 class="serif" style="margin:22px 0 18px;width:760px;font-size:100px;line-height:0.94;color:{PIZ}">Ahí sí es <span style="background:#FFFDF8;padding:0 10px">liquidación</span></h2>
<p style="margin:0 0 60px;width:700px;font-size:31px;line-height:1.42;color:{PIZ}">Es el finiquito <b>más</b> una indemnización. Lo básico que marca la ley:</p>
<div style="display:flex;gap:12px;align-items:center">
{bloque("Finiquito", "lo que ya ganó", "#FFFDF8", INK, -1.5)}{mas}
{bloque("3 meses", "de salario", PIZ, "#F4F1EA", 1.2)}{mas}
{bloque("12 días", "por año de prima de antigüedad", "#B7CFE6", INK, -1)}
</div>
<div class="hoja" style="margin-top:70px;padding:36px 40px;color:{INK};transform:rotate(0.6deg);box-shadow:0 16px 30px rgba(30,36,44,0.18)">
<div class="kicker" style="font-size:19px;color:#C98F7E">Y PUEDE CRECER</div>
<div style="font-size:27px;line-height:1.42;margin-top:12px">En algunos casos se suman <b>20 días por cada año</b> trabajado. Y si llega a juicio y no pruebas la causa del despido, también <b>salarios vencidos de hasta 12 meses</b>.</div>
</div>
<p style="margin:56px 0 0;font-size:27px;line-height:1.4;color:{PIZ}">En el despido, la prima de antigüedad se paga sin importar cuántos años tenga.</p>
</div>
{foot("Fuente: arts. 48, 50 y 162 fr. III LFT · " + H, 4, TOT)}""", " background: #D9B4A8;")))

# 5. ¿Cuál te toca? (papel) dos columnas
def item(t, c):
    return (f'<div style="display:flex;gap:16px;align-items:flex-start;padding:22px 0;border-bottom:1px solid rgba(43,53,66,0.15)">'
            f'<div style="flex:none;width:16px;height:16px;margin-top:13px;border-radius:50%;background:{c}"></div>'
            f'<div style="font-size:29px;line-height:1.35;color:{INK}">{t}</div></div>')
colF = item("Renuncia voluntaria.", "#A9C9A9") + item("Se acaba el contrato por tiempo u obra determinada.", "#A9C9A9") + item("Lo terminan de mutuo acuerdo.", "#A9C9A9")
colL = item("Despido sin una causa justificada.", "#C98F7E") + item("Despido con causa, pero <b>sin aviso por escrito</b>: se presume injustificado.", "#C98F7E") + item("La persona se va por una falta grave del patrón.", "#C98F7E")
S.append(("Leg3-05-Cual", page("Cuál te toca", "bg-papel", INK, f"""
<div style="position:absolute;left:90px;right:90px;top:100px">
<div class="kicker" style="color:#5F7E9E;font-weight:700">DEPENDE DE CÓMO TERMINA</div>
<h2 class="serif" style="margin:22px 0 60px;font-size:88px;line-height:0.95;color:{PIZ}">¿Cuál te <span style="{MK('#B7CFE6')}">toca pagar?</span></h2>
<div style="display:flex;gap:30px;align-items:flex-start">
  <div class="hoja" style="flex:1;padding:26px 28px 14px;transform:rotate(-1.2deg);box-shadow:0 16px 30px rgba(30,36,44,0.16);border-top:10px solid #A9C9A9">
    <div class="serif" style="font-size:44px;line-height:1;color:{PIZ}">Finiquito</div>{colF}
  </div>
  <div class="hoja" style="flex:1;padding:26px 28px 14px;transform:rotate(1deg);box-shadow:0 16px 30px rgba(30,36,44,0.16);border-top:10px solid #C98F7E;margin-top:30px">
    <div class="serif" style="font-size:44px;line-height:1;color:{PIZ}">Liquidación</div>{colL}
  </div>
</div>
<div style="margin-top:80px;display:flex;gap:20px;align-items:flex-start;padding:26px 30px;background:{PIZ};color:#F4F1EA;transform:rotate(-0.5deg);box-shadow:0 16px 30px rgba(30,36,44,0.2)">
<svg aria-hidden="true" width="36" height="36" viewBox="0 0 24 24" style="flex:none;margin-top:3px"><circle cx="12" cy="12" r="11" fill="#B7CFE6"/><path d="M12 6.5v7M12 16.8v.5" fill="none" stroke="#262F3B" stroke-width="2.4" stroke-linecap="round"/></svg>
<div style="font-size:28px;line-height:1.42">El aviso de despido va por escrito, con la conducta y las fechas, y se entrega en ese momento o al Tribunal dentro de los 5 días hábiles siguientes.</div>
</div>
</div>
{foot("Fuente: arts. 47, 51, 52 y 53 LFT · " + H, 5, TOT)}""")))

# 6. Antes de firmar (sarga oscura): lámina tipo lista
lista = [("Por escrito", "con lo que lo motiva"), ("Desglosado", "concepto por concepto"), ("Ratificado", "ante el Centro de Conciliación"), ("Sin renuncias", "a lo que ya ganó")]
ll = "".join(
    f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:30px 0;border-top:2px solid rgba(244,241,234,0.25)">'
    f'<div class="serif" style="font-size:96px;line-height:0.95;color:{c}">{t}</div><div style="flex:none;width:250px;text-align:right;font-size:23px;line-height:1.3;color:rgba(244,241,234,0.78)">{d}</div></div>'
    for (t, d), c in zip(lista, ["#F4F1EA", "#B7CFE6", "#F4F1EA", "#D9B4A8"]))
S.append(("Leg3-06-Firmar", page("Antes de firmar", "bg-sarga", "#F4F1EA", f"""
<div aria-hidden="true" style="position:absolute;left:40px;top:675px;transform:translate(-50%,-50%) rotate(-90deg);white-space:nowrap;font-size:17px;font-weight:700;letter-spacing:0.3em;color:rgba(244,241,234,0.5)">ANTES DE FIRMAR · ART. 33 LFT</div>
<div style="position:absolute;left:100px;right:90px;top:100px">
<div class="kicker" style="color:#A9C9A9;font-weight:700">EL CONVENIO DE SALIDA</div>
<h2 class="serif" style="margin:22px 0 40px;font-size:66px;line-height:1;width:800px">Para que valga y no te lo reclamen después, que sea:</h2>
{ll}
<div style="border-top:2px solid rgba(244,241,234,0.25)"></div>
<div class="hoja" style="margin-top:40px;padding:28px 34px;color:{INK};transform:rotate(-0.8deg);box-shadow:0 20px 36px rgba(0,0,0,0.35)">
<div style="font-size:29px;line-height:1.42"><b>Ojo:</b> que firme una renuncia no borra lo que ya ganó. La ley dice que esa renuncia <b>es nula</b>, se llame como se llame.</div>
</div>
</div>
{foot("Fuente: art. 33 LFT · " + H, 6, TOT, True)}""")))

# 7. Cierre
S.append(("Leg3-07-Cierre", cierre("¿Ya sabes cuál", "te toca pagar?",
    "En GGTZ te ayudamos con tu empresa: constitución, marcas, contratos y temas laborales.",
    "Agenda tu asesoría", "Comenta <b>FINIQUITO</b> y guarda este post para cuando lo necesites.", fondo="atardecer")))

for name, html in S:
    (HERE / f"{name}.dc.html").write_text(html)
print("ok", len(S))
