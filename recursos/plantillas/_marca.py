# Piezas compartidas de la identidad de marca (13 oct 2026): fondos degradados y logos.
# Uso: import desde cualquier generador con importlib (ver _gen_oct20_22.py) o copiar la función.

LOGO_H_MARFIL = "/_blob/916dbd49a3cb1e203b606fc4f660fbea"
LOGO_H_PIZARRA = "/_blob/7afe418b8551e87bb3f0f8e196d8230f"
SELLO_MARFIL = "/_blob/5b8391f45478910a1d0d8ca2823faf9b"
SELLO_PIZARRA = "/_blob/89b150b4a0eaffd521105fa61198e074"

# Cada degradado: color base + manchas (x, y, ancho, alto, color, desenfoque) en una lámina de 1080x1350.
# Oscuros (texto marfil): sierra, noche, atardecer, neblina (arriba oscuro, abajo claro).  Claros (texto tinta): salvia, bruma.
GRADIENTES = {
    "sierra": ("#1C2027", [(-350, -250, 750, 1100, "#E2B48F", 110), (-80, -200, 700, 600, "#C98F7E", 120), (120, -80, 900, 520, "#3E5C9A", 120),
                           (-330, 650, 620, 900, "#D8A784", 120), (-100, 900, 650, 500, "#2F4A86", 120)]),
    "noche": ("#151B23", [(450, -350, 1000, 900, "#7FA3C4", 140), (650, -150, 600, 500, "#B7CFE6", 110), (-300, 900, 700, 600, "#C98F7E", 160),
                          (-200, 300, 800, 700, "#1F2E40", 120)]),
    "atardecer": ("#1A2129", [(-250, -300, 900, 700, "#3E5C9A", 140), (500, 700, 900, 900, "#C98F7E", 150), (650, 950, 600, 500, "#E2B48F", 130),
                              (-300, 500, 800, 600, "#1F2E40", 120)]),
    "neblina": ("#1C2B38", [(-200, -150, 1200, 900, "#2D5566", 140), (-300, 250, 1000, 700, "#152635", 120), (300, 700, 1100, 600, "#5F8FA6", 150),
                            (-200, 950, 1500, 700, "#E9EEF2", 120), (500, 1000, 700, 500, "#B7CFE6", 110)]),
    "salvia": ("#EEF0EA", [(-250, -250, 900, 800, "#A9C9A9", 130), (500, -100, 800, 700, "#B7CFE6", 130), (200, 600, 900, 700, "#F4F1EA", 120),
                           (-200, 900, 800, 600, "#CFE0CF", 120), (650, 950, 600, 500, "#D9B4A8", 140)]),
    "bruma": ("#F1F2F2", [(-300, -200, 1000, 700, "#C9DAEA", 130), (500, 300, 800, 800, "#F4F1EA", 120), (-200, 800, 900, 700, "#E3D2CB", 140),
                          (600, 1000, 700, 500, "#B7CFE6", 130)]),
}

def grad(nombre, h=1350):
    """Capa de fondo degradado para meter como PRIMER hijo de la lámina.
    La lámina debe llevar `isolation: isolate` (la capa va con z-index -1 para quedar debajo de todo)."""
    base, manchas = GRADIENTES[nombre]
    k = h / 1350
    capas = "".join(
        f'<div style="position:absolute;left:{x}px;top:{round(y*k)}px;width:{w}px;height:{round(hh*k)}px;border-radius:50%;background:{c};filter:blur({b}px)"></div>'
        for x, y, w, hh, c, b in manchas)
    ruido = ('<svg width="1080" height="%d" style="position:absolute;inset:0;opacity:0.16;mix-blend-mode:overlay">'
             '<filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/></filter>'
             '<rect width="100%%" height="100%%" filter="url(#gr)"/></svg>') % h
    return f'<div aria-hidden="true" style="position:absolute;inset:0;z-index:-1;overflow:hidden;background:{base}">{capas}{ruido}</div>'
