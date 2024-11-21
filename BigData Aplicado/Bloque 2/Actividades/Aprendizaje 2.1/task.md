# Apartado 1

### En el apartado 5.5 hemos visto cómo escribir el código Pig Latin para contar las veces que aparece cada palabra de un archivo de texto. En este ejercicio, debes contar las ocurrencias de todas las palabras que comienzan y terminan por una letra "a" minúscula en el archivo quijote.txt que ya hemos empleado en los apuntes.

# Apartado 2

### Descarga el fichero CSV con los datos de los alojamientos turísticos de Mallorca del catálogo de datos abiertos del Govern de las Illes Balears: [alojamientos turísticos de Mallorca](https://intranet.caib.es/opendatacataleg/dataset/b836d52a-c127-4837-b945-5383d8d8ea85/resource/5a1bc964-8207-41d0-a4a1-5a5ddebf1deecs/download).

### También puedes descargar el archivo directamente desde [repositorio github Toni](https://raw.githubusercontent.com/tnavarrete-iedib/bigdata-24-25/refs/heads/main/mapa-alojamiento-turistics-mallorca.csv).

### Con estos datos, escribe el código Pig Latin para implementar estas consultas de análisis:

1. #### Muestra el número de filas de datos que hay en total (no se debe contar la cabecera)

1. #### Muestra el número de plazas que hay en el municipio de Palma

1. #### Muestra la media del número de habitaciones de los hoteles (subgrupo hotel) del municipio de Manacor

1. #### Muestra el número de plazas de cada tipo de alojamiento (subgrupos), ordenados de mayor a menor número de plazas

1. #### Muestra el número de alojamientos de más de 200 plazas de cada categoría, ordenados de mayor a menor número de alojamientos

1. #### Muestra los tres municipios que más habitaciones de agroturismo tienen (y su número de habitaciones), ordenados de mayor a menor número de habitaciones.

1. #### Exporta a un archivo el número de habitaciones totales de cada municipio, ordenados alfabéticamente por municipio

1. #### Exporta a un archivo los siguientes campos de los 10 alojamientos de 3 estrellas que tienen más habitaciones:
   -  #### Denominación comercial
   -  #### Municipio
   -  #### Plazas
   -  #### Número de habitaciones
