# Econexus

**Datos de la Bolsa Mercantil, conectados.**

Econexus reúne en una sola página doce tableros interactivos sobre los mercados de la Bolsa Mercantil de Colombia (BMC) y su contexto económico, organizados en cuatro pestañas: MERCOP, MCP, Atra-e e IPAP.

Ver en línea: https://syrodelus.github.io/Econexus/

## Tableros

| Pestaña | Posición | Archivo | Qué muestra |
|---|---|---|---|
| MERCOP | 1 | `Mercop/mercop_mapa.html` | Valor negociado en el Mercado de Comercialización entre Privados por departamento |
| MERCOP | 2 | `Mercop/mercop_grafico.html` | Valor negociado en MERCOP por año |
| MERCOP | 3 | `Mercop/mercop_pastel.html` | Negociación en MERCOP por tipo de emisor |
| MCP | 1 | `MCP/mcp_eficiencia.html` | Mercado de Compras Públicas: presupuesto oficial frente a valor adjudicado y ahorros reportados |
| MCP | 2 | `MCP/mcp_riesgos.html` | Ejecución de las operaciones: adiciones, prórrogas e incumplimientos por categoría o entidad |
| MCP | 3 | `MCP/mcp_valor_negociado.html` | Valor negociado en el MCP por trimestre |
| Atra-e | 1 | `Atra-e/atrae_grafico.html` | Valor negociado en Atra-e (facturas electrónicas) por trimestre |
| Atra-e | 2 | `Atra-e/atrae_pastel.html` | Negociación en Atra-e por tipo de emisor |
| Atra-e | 3 | `Atra-e/atrae_calculadora.html` | Simulador de negociación de facturas para vendedor y comprador |
| IPAP | 1 | `Ipap/area_agricola_mapa.html` | Área cultivada y área cultivable por departamento |
| IPAP | 2 | `Ipap/poblacion_colombia_grafico.html` | Población de Colombia (proyecciones del DANE) |
| IPAP | 3 | `Ipap/ipap_vs_ipc_grafico.html` | Índice de Precios Agropecuarios (IPAP) de la BMC frente al IPC del DANE |

## Datos y fuentes

- **Cada gráfica trae sus propias fuentes y datos.** Al pie de cada tablero se indica la fuente, y el botón **"Descargar datos (.xlsx)"** baja un Excel con los datos de la gráfica, sus fuentes (con enlaces) y las notas de cálculo.
- **Los datos ya están dentro del código.** Cada archivo HTML lleva incrustados sus datos, fuentes y notas, así que no depende de archivos externos ni de bases de datos. Por eso el repositorio no incluye una carpeta de datos aparte.
- Las fuentes principales son la Bolsa Mercantil de Colombia, el DANE, el Ministerio de Agricultura (Agronet), la UPRA y la Secretaría Distrital de Planeación de Bogotá. El detalle de cada cifra está en la descarga de cada tablero.

## Estructura

```
index.html            Página completa: encabezado, pestañas y los 12 tableros incrustados
Mercop/  MCP/  Atra-e/  Ipap/
                      Los 12 tableros originales, cada uno funciona también por separado
herramientas/
  plantilla.html      Encabezado, pestañas y distribución de index.html
  construir.py        Vuelve a generar index.html a partir de los tableros
```

`index.html` contiene una copia de cada tablero. Si editas un archivo de las carpetas, vuelve a generar la página completa:

```
python herramientas/construir.py
```

Solo necesita Python 3, sin librerías adicionales.

## Cómo funciona

- Cada tablero se carga dentro de la página en su propio marco, para que sus estilos y scripts no choquen entre sí. Se carga la primera vez que abres su pestaña.
- En computador, los bloques vecinos se igualan en altura y ancho. En celular (menos de 720 px), todo pasa a una sola columna.
- Cada pestaña tiene su propio enlace: `#mercop`, `#mcp`, `#atrae` e `#ipap`.
- Las gráficas usan Chart.js y las descargas usan SheetJS, ambos cargados desde CDN. Por eso la página necesita conexión a internet.
