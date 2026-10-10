# Anuncio pagado "Te ayudo con tus impuestos" (Ad-*): feed 1080x1350 y story 1080x1920
import importlib.util, pathlib, io, contextlib
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("base", HERE / "_gen_oct20_22.py")
base = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(base)
page, B = base.page, base.B

PHONE_ICON = '<svg aria-hidden="true" width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#262F3B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"></path></svg>'

def card(k, t, d, bg, fg, rot):
    return (f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 10px; padding: 30px 28px; background: {bg}; color: {fg}; transform: rotate({rot}deg); box-shadow: 0 16px 30px rgba(0,0,0,0.35)">'
            f'<div class="kicker" style="font-size: 17px; opacity: 0.8">{k}</div><div class="serif" style="font-size: 46px; line-height: 1">{t}</div><div style="font-size: 22px; line-height: 1.35; opacity: 0.85">{d}</div></div>')

def body(h, top_title, cards_top, cta_top, photo_w, k=1.0):
    return f"""
<div aria-hidden="true" style="position: absolute; right: -60px; bottom: -40px; width: {photo_w + 40}px; height: {photo_w + 40}px; border-radius: 50%; background: #A9C9A9"></div>
<img src="{B('berny')}" alt="Bernardo Latorre, Contador Público" style="position: absolute; right: -40px; bottom: 0; width: {photo_w}px; height: auto; filter: drop-shadow(0 18px 30px rgba(0,0,0,0.4))">
<div style="position: absolute; left: 70px; top: 70px; padding: 12px 22px; background: rgba(244,241,234,0.94); color: #2B3542; font-size: 20px; font-weight: 700; letter-spacing: 0.22em; transform: rotate(-2deg)">GGTZ CONSULTORES · MONTERREY</div>
<div style="position: absolute; left: 80px; right: 80px; top: {top_title}px; display: flex; flex-direction: column; gap: 22px">
<h1 class="serif" style="margin: 0; font-size: {int(112*k)}px; line-height: 0.9">Tus impuestos, <em style="font-style: italic; color: #B7CFE6">en orden</em></h1>
<p style="margin: 0; max-width: 820px; font-size: {int(32*k)}px; line-height: 1.4; color: rgba(244,241,234,0.9)">Te ayudo a cumplir con el SAT y a planear para pagar lo justo.</p>
</div>
<div style="position: absolute; left: 80px; width: 600px; top: {cards_top}px; display: flex; gap: 18px">
{card('PERSONAS', 'Físicas', 'Honorarios, RESICO, arrendamiento, asalariados', '#F4F1EA', '#1E242C', -2)}{card('PERSONAS', 'Morales', 'Empresas y PyMEs: contabilidad, declaraciones y planeación', '#B7CFE6', '#1E242C', 2)}
</div>
<div style="position: absolute; left: 80px; top: {cta_top}px; width: 470px; display: flex; flex-direction: column; gap: 20px">
<div class="serif" style="font-size: {int(54*k)}px; line-height: 1.05">Platícame <em style="font-style: italic; color: #B7CFE6">tu proyecto</em></div>
<div style="display: inline-flex; align-self: flex-start; align-items: center; gap: 18px; padding: 22px 32px; background: #F4F1EA; color: #262F3B; border-radius: 6px; box-shadow: 0 14px 26px rgba(0,0,0,0.35)">{PHONE_ICON}<span style="font-size: 46px; font-weight: 700; letter-spacing: 0.02em">81 2758 0277</span></div>
<div style="font-size: 22px; line-height: 1.4; color: rgba(244,241,234,0.75)">Bernardo Latorre · Contador Público<br>8 años en Big Four</div>
</div>
"""

feed = page("Anuncio · Feed", "bg-sarga", "#F4F1EA", body(1350, 170, 610, 900, 560))
story = page("Anuncio · Story", "bg-sarga", "#F4F1EA", body(1920, 300, 800, 1170, 700, 1.15))
story = story.replace("height: 1350px", "height: 1920px").replace('"height":1350', '"height":1920')
(HERE / "Ad-01-Feed.dc.html").write_text(feed)
(HERE / "Ad-02-Story.dc.html").write_text(story)
print("ok")
