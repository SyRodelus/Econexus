"""Vuelve a generar index.html a partir de los 12 tableros de las carpetas.

Uso (desde la raíz del repositorio):
    python herramientas/construir.py

Lee herramientas/plantilla.html, incrusta cada tablero (codificado en base64 para que
sus scripts no choquen entre sí) y escribe index.html. Solo usa la biblioteca estándar.
"""
import base64
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent

TABLEROS = {
    'mercop_mapa': 'Mercop/mercop_mapa.html',
    'mercop_grafico': 'Mercop/mercop_grafico.html',
    'mercop_pastel': 'Mercop/mercop_pastel.html',
    'mcp_eficiencia': 'MCP/mcp_eficiencia.html',
    'mcp_riesgos': 'MCP/mcp_riesgos.html',
    'mcp_valor_negociado': 'MCP/mcp_valor_negociado.html',
    'atrae_grafico': 'Atra-e/atrae_grafico.html',
    'atrae_pastel': 'Atra-e/atrae_pastel.html',
    'atrae_calculadora': 'Atra-e/atrae_calculadora.html',
    'area_agricola_mapa': 'Ipap/area_agricola_mapa.html',
    'poblacion_colombia_grafico': 'Ipap/poblacion_colombia_grafico.html',
    'ipap_vs_ipc_grafico': 'Ipap/ipap_vs_ipc_grafico.html',
}


def main():
    bloques = []
    for clave, ruta in TABLEROS.items():
        contenido = (RAIZ / ruta).read_bytes()
        b64 = base64.b64encode(contenido).decode('ascii')
        bloques.append(f'<script type="text/plain" id="src-{clave}">{b64}</script>')
    plantilla = (RAIZ / 'herramientas' / 'plantilla.html').read_text(encoding='utf-8')
    salida = plantilla.replace('__SOURCES__', '\n'.join(bloques))
    (RAIZ / 'index.html').write_text(salida, encoding='utf-8')
    print(f'index.html generado ({len(salida):,} caracteres, {len(TABLEROS)} tableros)')


if __name__ == '__main__':
    main()
