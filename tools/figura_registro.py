"""Dibuja `assets/register.svg` DESDE el registro. La figura tampoco se teclea a mano.

**Por qué existe.** El §2 del registro llegó a decir tres cifras distintas a la vez porque el
recuento se mantenía a mano, y `recuento_auditoria.py` existe para que ese número lo genere una
máquina. Una figura es un recuento más: si las 93 casillas de la portada se dibujaran a mano,
volverían a divergir del documento en cuanto cambiara una fila — y esta vez nadie lo notaría,
porque un dibujo no se relee. Así que la figura la genera el mismo parseo que el recuento, y el
CI comprueba que la que está publicada es la que sale de las tablas de hoy.

    python tools/figura_registro.py            # reescribe assets/register.svg
    python tools/figura_registro.py --check    # rc=1 si la publicada no es la que toca

**Lo que esta figura NO dice.** Nada sobre eficacia comparada. 93 es el denominador de lo
REGISTRADO, no de los errores cometidos, y cada descubridor tuvo un número distinto —y
desconocido— de oportunidades. Las columnas no se pueden ordenar por mérito.
"""
import argparse
import io
import os
import sys

_AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _AQUI)
import recuento_auditoria as R                                       # noqa: E402

DOC = os.path.join(os.path.dirname(_AQUI), "register", "AUDITORIA_DEL_METODO.md")
SVG = os.path.join(os.path.dirname(_AQUI), "assets", "register.svg")

# Los seis grupos con más de una entrada, con el nombre que el README usa en inglés. El resto de
# etiquetas —una entrada cada una— van juntas en gris: separarlas en catorce colores sería dar
# apariencia de estructura a lo que son casos sueltos.
GRUPOS = [
    ("REV-EXT",           "#E8A33D", "an external human reviewer"),
    ("AUTOR",             "#4A90D9", "the author, on his own criterion"),
    ("REV-ADV",           "#3FB950", "an automated adversarial review"),
    ("ARNÉS",             "#9B59B6", "the mutation harness"),
    ("CI",                "#17A2B8", "continuous integration"),
    ("el propio revisor", "#C0392B", "the reviewer, about his own claim"),
]
OTROS = ("#5A6674", "eight further labels, one entry each")
COL, LADO, HUECO, X0, Y0 = 16, 34, 6, 60, 150


def casillas(filas):
    """Una casilla por entrada, agrupadas por descubridor y en el orden de `GRUPOS`."""
    por_grupo = {k: [] for k, _, _ in GRUPOS}
    sueltas = []
    for id_, desc in filas:
        clave = desc.split(",")[0].split("+")[0].strip()
        (por_grupo[clave] if clave in por_grupo else sueltas).append(id_)
    orden = []
    for k, color, _ in GRUPOS:
        orden += [(i, color) for i in por_grupo[k]]
    orden += [(i, OTROS[0]) for i in sueltas]
    return orden, {k: len(por_grupo[k]) for k, _, _ in GRUPOS}, len(sueltas)


def svg(orden, cuentas, n_sueltas, n_e, n_x):
    filas_alto = (len(orden) + COL - 1) // COL
    alto = Y0 + filas_alto * (LADO + HUECO) + 96
    L = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {alto}" width="1200" '
         f'height="{alto}" role="img" aria-label="{len(orden)} squares, one per false claim in the '
         f'register, coloured by who or what caught it.">',
         f'  <rect width="1200" height="{alto}" fill="#12161C"/>',
         '  <text x="60" y="58" font-family="Georgia, serif" font-size="26" fill="#F2F4F7">'
         f'{len(orden)} claims, and who caught each one</text>',
         '  <text x="60" y="86" font-family="Georgia, serif" font-size="15" font-style="italic" '
         f'fill="#8B98A8">One square per entry in the register: {n_e} claims made by the author, '
         f'{n_x} made by the external reviewer.</text>',
         '  <text x="60" y="112" font-family="Georgia, serif" font-size="15" font-style="italic" '
         'fill="#8B98A8">The colour is the discoverer. The columns cannot be ranked: each mechanism '
         'had a different, unknown number of chances.</text>']
    for n, (id_, color) in enumerate(orden):
        x = X0 + (n % COL) * (LADO + HUECO)
        y = Y0 + (n // COL) * (LADO + HUECO)
        L.append(f'  <rect x="{x}" y="{y}" width="{LADO}" height="{LADO}" rx="3" fill="{color}">'
                 f'<title>{id_}</title></rect>')
    # leyenda, a la derecha de la cuadrícula
    lx = X0 + COL * (LADO + HUECO) + 40
    ly = Y0 + 16
    for k, color, etiqueta in GRUPOS:
        L.append(f'  <rect x="{lx}" y="{ly - 13}" width="15" height="15" rx="2" fill="{color}"/>')
        L.append(f'  <text x="{lx + 26}" y="{ly}" font-family="Georgia, serif" font-size="15" '
                 f'fill="#C9D2DD">{etiqueta}</text>')
        L.append(f'  <text x="1140" y="{ly}" font-family="Georgia, serif" font-size="15" '
                 f'fill="#F2F4F7" text-anchor="end">{cuentas[k]}</text>')
        ly += 30
    L.append(f'  <rect x="{lx}" y="{ly - 13}" width="15" height="15" rx="2" fill="{OTROS[0]}"/>')
    L.append(f'  <text x="{lx + 26}" y="{ly}" font-family="Georgia, serif" font-size="15" '
             f'fill="#C9D2DD">{OTROS[1]}</text>')
    L.append(f'  <text x="1140" y="{ly}" font-family="Georgia, serif" font-size="15" '
             f'fill="#F2F4F7" text-anchor="end">{n_sueltas}</text>')
    ly += 34
    L.append(f'  <line x1="{lx}" y1="{ly - 26}" x2="1140" y2="{ly - 26}" stroke="#2A323D"/>')
    L.append(f'  <text x="{lx + 26}" y="{ly}" font-family="Georgia, serif" font-size="15" '
             f'fill="#8B98A8">total</text>')
    L.append(f'  <text x="1140" y="{ly}" font-family="Georgia, serif" font-size="15" '
             f'fill="#F2F4F7" text-anchor="end">{len(orden)}</text>')
    pie = alto - 40
    L.append(f'  <line x1="60" y1="{pie - 28}" x2="1140" y2="{pie - 28}" stroke="#2A323D"/>')
    L.append(f'  <text x="60" y="{pie}" font-family="Georgia, serif" font-size="14" '
             'font-style="italic" fill="#8B98A8">Missing from this picture, by construction: the '
             'claims nobody ever caught. Those are the interesting ones.</text>')
    L.append("</svg>")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="no escribe; rc=1 si la figura esta rancia")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

    texto = io.open(DOC, encoding="utf-8").read()
    e, x, _ = R.recuento(texto)                 # reusa el parseo Y el rechazo de ids duplicados
    orden, cuentas, n_sueltas = casillas(e + x)
    nuevo = svg(orden, cuentas, n_sueltas, len(e), len(x))
    print(f"  entradas en el registro .. {len(orden)}  ({len(e)} del autor, {len(x)} del revisor)")
    for k, _, etiqueta in GRUPOS:
        print(f"     {etiqueta:38} {cuentas[k]}")
    print(f"     {OTROS[1]:38} {n_sueltas}")

    viejo = io.open(SVG, encoding="utf-8").read() if os.path.exists(SVG) else None
    if viejo == nuevo:
        print("\n  FIGURA AL DIA")
        return 0
    if args.check:
        print("\n  FIGURA RANCIA — corre sin --check para regenerarla")
        return 1
    io.open(SVG, "w", encoding="utf-8", newline="\n").write(nuevo)
    print("\n  figura REGENERADA desde las tablas del registro")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
