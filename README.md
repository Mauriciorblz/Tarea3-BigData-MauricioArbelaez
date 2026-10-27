# Tarea3-BigData-MauricioArbelaez
Análisis histórico de la TRM en Colombia mediante procesamiento batch con Apache Spark y Hadoop.
# Análisis de la TRM en Colombia con Apache Spark

**Autor:** Mauricio Arbeláez  
**Universidad:** Universidad Nacional Abierta y a Distancia (UNAD)  
**Curso:** Big Data – 202016911  
**Actividad:** Tarea 3

## Propósito del ejercicio

Este proyecto  tiene como finalidad examinar el comportamiento histórico de la Tasa Representativa del Mercado (TRM) en Colombia, utilizando herramientas de procesamiento de datos como Apache Spark y Hadoop.

Para desarrollar el análisis, utilicé un programa en Python que permitió consultar los registros históricos, preparar la información y calcular indicadores estadísticos como el promedio, el valor mínimo y el valor máximo de la tasa de cambio.

## Información analizada

Los datos provienen del conjunto **Tasa de Cambio Representativa del Mercado – Histórico**, publicado en el Portal de Datos Abiertos de Colombia.

El archivo utilizado se denomina `trm_actual.csv` y fue almacenado en Hadoop HDFS, dentro del directorio `/Tarea3/`.

La información incluye el valor de la tasa de cambio, su unidad de referencia y las fechas de vigencia de cada registro.

## Desarrollo de la práctica

El procesamiento se realizó en una máquina virtual Ubuntu, utilizando Hadoop como sistema de almacenamiento y Apache Spark como herramienta de análisis.

El programa `trm_batch.py` permite:

- Acceder al archivo CSV almacenado en HDFS.
- Consultar los primeros registros del conjunto de datos.
- Examinar la estructura de la información.
- Preparar los valores numéricos y las fechas para su análisis.
- Excluir registros que no contienen los datos necesarios.
- Obtener estadísticas generales de la TRM.
- Identificar los diez registros con los valores más elevados.

## Ejecución del programa

Para reproducir el ejercicio se requiere un entorno con Python, PySpark y acceso a Hadoop HDFS.

El archivo de datos debe estar disponible en la ruta:

`hdfs://localhost:9000/Tarea3/trm_actual.csv`

Desde la terminal de Ubuntu, en el directorio donde se encuentra el programa, se ejecuta:

`python3 trm_batch.py`

Los resultados se presentan directamente en la terminal.

## Resultados de mi análisis

Durante la ejecución se procesaron **8.374 registros** históricos.

Los indicadores obtenidos fueron:

| Indicador | Resultado |
|---|---|
| Cantidad de registros | 8.374 |
| Promedio de la TRM | 2.373,30 COP |
| Valor mínimo | 620,62 COP |
| Valor máximo | 5.061,21 COP |

Estos resultados evidencian que la tasa de cambio ha presentado diferencias importantes entre los periodos registrados. La identificación de los valores extremos permite reconocer momentos de mayor y menor cotización del dólar dentro de la información disponible.

## Aprendizaje obtenido

La práctica me permitió comprender cómo se relacionan el almacenamiento distribuido y el procesamiento de datos. También pude aplicar operaciones de limpieza, transformación y análisis estadístico mediante Apache Spark.

El ejercicio demuestra que estas herramientas pueden utilizarse para estudiar información económica y obtener resultados que faciliten su interpretación.
