# Guía de estilo: carruseles @bernardolatorre.fiscal

Estándar aprobado por Berny el 9 de octubre de 2026 (versión "v2": Cierre fiscal y RESICO). **Todo carrusel nuevo se hace así**, pero cada uno debe traer algo distinto y nuevo. Las plantillas de referencia están en `recursos/plantillas/` (Cie-* y Res-*).

## Lo que no cambia

- **Formato:** 1080×1350 px, de 7 a 9 láminas. Se renderiza con `python3 recursos/render.py <carpeta_plantillas> <carpeta_salida> <archivos.dc.html>`.
- **Paleta:**
  - Pizarra #262F3B / #2B3542.
  - Marfil #F4F1EA / #FFFDF8.
  - Azul polvo #B7CFE6 como acento principal.
  - Salvia #A9C9A9 y terracota suave #D9B4A8 / #C98F7E como acentos secundarios.
  - Texto en #1E242C. **Nunca dorado.**
- **Tipografía:** Instrument Serif para los títulos (con una palabra clave en cursiva) y Hanken Grotesk para el texto. Las etiquetas pequeñas van en mayúsculas con letter-spacing de 0.24em.
- **Portada:** nunca lleva la foto de Berny. Su foto (sticker recortado) aparece solo en la última lámina, junto al botón para agendar.
- **Última lámina:**
  - Una foto real de Monterrey en una banda superior.
  - Una pregunta en grande.
  - Un botón de llamada a la acción.
  - Una tarjeta que invite a comentar o a guardar.
  - "81 2758 0277 · @bernardolatorre.fiscal" y el logotipo GGTZ CONSULTORES.
- **Pie de cada lámina:** la fuente legal ("Fuente: art. X LISR"), el usuario de Instagram y la numeración "03 / 08".
- **Datos:** toda cifra o artículo se verifica en la ley vigente (Luthor o una fuente oficial) o en el DOF y el SAT antes de usarse.
- **Imágenes:**
  - Solo del banco `recursos/` (fotos de Unsplash con licencia libre, capturas del SAT) o fotos nuevas de Unsplash con licencia libre, nunca de Google.
  - Las capturas del SAT siempre van dentro de un marco de navegador o de celular y con contexto educativo.
  - No usar fotos con texto en inglés, ni moneda o formularios de otros países.

## Ritmo visual (para que no se vea plano)

- **Alternar fondos.** Nunca dos láminas seguidas con el mismo fondo. Las opciones son:
  - Lino claro (`.bg-lino`).
  - Papel cuadriculado (`.bg-papel`).
  - Sarga oscura (`.bg-sarga`).
  - Foto a todo lo ancho con degradado pizarra.
  - Bloque de color sólido.
- **Por carrusel, como mínimo:**
  - 3 fotos reales.
  - 1 captura de pantalla real (del SAT, el DOF, el IMSS o Banxico) si el tema lo permite.
  - 1 lámina oscura.
  - 1 lámina con un número grande como protagonista.
- **Inclinar elementos.** Tarjetas, polaroids y stickers van rotados entre -6° y 6°. Se pueden agregar cinta adhesiva (washi tape), sombras y elementos que se salgan del margen.

## Catálogo de piezas (combinar y rotar)

| Pieza | Descripción | Usada en |
|---|---|---|
| Foto a todo lo ancho + tarjeta "hoja" rotada | Portada con título sobre papel | Cie-01 |
| Foto girada + tarjeta + sticker con cifra | Portada con dato | Res-01 |
| Número gigante + barra de meses | Fecha o cifra protagonista | Cie-02 |
| Lista de verificación en hoja + polaroid | Pasos o requisitos | Cie-03 |
| Cuadrícula 2×2 + recuadro oscuro + captura en navegador | Comparativo con prueba real | Cie-04 |
| Foto de fondo + tarjetas de vidrio con datos | Datos sobre ambiente | Cie-05 |
| Línea de tiempo oscura + celular con captura | Calendario o fechas límite | Cie-06 |
| Tabla oscura con barras | Tasas o rangos | Res-03 |
| Fórmula en bloques (A × B = C) | Explicar un cálculo | Res-02 |
| Tres polaroids con pie de foto | Perfiles de quién aplica | Res-04 |
| Ejemplo numérico: "Cobras $X → pagas $Y" | Caso práctico | Res-07 |
| Dos columnas: "Te conviene si / Compara si" | Decisión | Res-07 |

**Piezas nuevas para estrenar** (usar al menos una que no se haya usado antes en cada carrusel y agregarla a esta tabla):

- Mito contra realidad, con un sello "FALSO" o "CIERTO".
- Encuesta o quiz en lámina: "¿Cuál crees que es?", con la respuesta en la siguiente lámina.
- Recibo o ticket dibujado con un desglose de cifras.
- Antes y después, o error contra acierto, con una tachadura.
- Mapa de México o de Nuevo León con un dato.
- Conversación de chat (WhatsApp) con la duda de un cliente.
- Termómetro o semáforo de riesgo.
- Cuenta regresiva de días.
- Notas adhesivas (post-it) con tips.
- Captura de un titular del DOF dentro de un marco.
- Gráfica de barras o de línea con datos reales (inflación de INEGI, tipo de cambio de Banxico, UMA).
- Recorte de periódico simulado, sin marcas reales de medios.
- Lámina "Guárdalo para después", con una lista resumida.

## Ganchos y texto (tendencias 2026)

- **Primera lámina:** una pregunta o una promesa concreta, en 6 palabras o menos ("¿Te conviene el RESICO?", "Cierra el año sin sorpresas"). Agregar un número cuando sea posible.
- **Llamada a la acción:** pedir que **guarden** o **comenten** (funciona mucho mejor que pedir "likes"). La pie de foto incluye una pregunta.
- **Pie de foto:** escrito con las palabras que la gente busca (SEO dentro de Instagram) y con 1 o 2 hashtags relevantes (máximo 5).
- **Tono:** cálido, directo y de tú, para personas físicas y PyMEs de México. Nada de lenguaje de abogado.
