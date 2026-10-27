from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Iniciar Spark
spark = SparkSession.builder \
    .appName("Analisis_TRM") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Ruta del archivo de la TRM almacenado en HDFS
file_path = "hdfs://localhost:9000/Tarea3/trm_actual.csv"

# Cargar el archivo CSV
df_raw = spark.read \
    .option("header", "true") \
    .option("inferSchema", "false") \
    .csv(file_path)

print("\n=== DATOS ORIGINALES ===")
df_raw.show(10, truncate=False)

print("\n=== ESTRUCTURA ORIGINAL ===")
df_raw.printSchema()

# Limpieza y transformación del valor de la TRM
df = df_raw.withColumn(
    "VALOR_NUM",
    F.col("VALOR").cast("double")
)

# Convertir las fechas
df = df.withColumn(
    "FECHA_DESDE",
    F.to_date(F.col("VIGENCIADESDE"), "dd/MM/yyyy")
).withColumn(
    "FECHA_HASTA",
    F.to_date(F.col("VIGENCIAHASTA"), "dd/MM/yyyy")
)

# Eliminar registros sin valor numérico
df_limpio = df.filter(F.col("VALOR_NUM").isNotNull())

print("\n=== CANTIDAD DE REGISTROS ===")
print("Registros originales:", df_raw.count())
print("Registros después de la limpieza:", df_limpio.count())

print("\n=== ESTADISTICAS DE LA TRM ===")
df_limpio.select("VALOR_NUM").summary().show()

print("\n=== PROMEDIO, MINIMO Y MAXIMO ===")
df_limpio.select(
    F.round(F.avg("VALOR_NUM"), 2).alias("PROMEDIO_TRM"),
    F.min("VALOR_NUM").alias("MINIMO_TRM"),
    F.max("VALOR_NUM").alias("MAXIMO_TRM")
).show()

print("\n=== 10 VALORES MAS ALTOS DE LA TRM ===")
df_limpio.select(
    "VALOR_NUM",
    "UNIDAD",
    "FECHA_DESDE",
    "FECHA_HASTA"
).orderBy(
    F.col("VALOR_NUM").desc()
).show(10, truncate=False)

print("\n=== ANALISIS FINALIZADO ===")

spark.stop()
