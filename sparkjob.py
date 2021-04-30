from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .master('local') \
    .appName('sparkjob-to-bq') \
    .getOrCreate()


bucket = "week-3-spark-job-dataproc"
spark.conf.set('temporaryGcsBucket', bucket)


files_name = ["2021-04-27","2021-04-28","2021-04-29","2021-04-30"]


for i in range(len(files_name)):
    file_name = files_name[i]
    for file_name in files_name:
        flight_data = spark.read.csv("gs://week-3-spark-job-dataproc/new_dataset/" + file_name + ".csv",
        header=True,
        sep=",",
        schema="flight_date string,airline_code string,flight_num integer,source_airport string,destination_airport string,departure_time integer,departure_delay integer,arrival_time integer,arrival_delay integer,airtime integer,distance integer,id string"
        )
        flight_data.createOrReplaceTempView("flights")
        sql_DF = spark.sql("""
            SELECT * FROM flights
        """)
        sql_DF.write.format("bigquery") \
            .option('table', "jomen034_sparkjob_dataproc." + file_name) \
            .save()

        if file_name == "2021-04-30":
            break

    if file_name == "2021-04-30":
        break