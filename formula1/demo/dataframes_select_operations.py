# Databricks notebook source
# MAGIC %md
# MAGIC ## Ingest circuites.csv file

# COMMAND ----------

# Include the common file to export the common variable and functions.
# The filename without extention is fine
# "/formula1/include/configuration"

# COMMAND ----------

# MAGIC %run "/formula1/include/configuration"

# COMMAND ----------

# MAGIC %run "/formula1/include/common_functions"

# COMMAND ----------

# Check the exported values are coming
display(raw_folder_path)

# COMMAND ----------

# Check the exported values are coming
processed_folder_path

# COMMAND ----------

# Utility for the Widget to take the input parameter.
dbutils.widgets.help()

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
# the default value is ""  , but it can be anything we defined.
dbutils.widgets.text("p_data_source","")
v_data_source = dbutils.widgets.get("p_data_source")
display(v_data_source)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1 : Read CSV file using the Spark Data frame reader

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

#The above dispaly is not good , hence use the display function to get the better display in table format.
display(dbutils.fs.mounts())

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/databrickscourcedl/raw

# COMMAND ----------

# read the CSV file from the actual point location referring to the ADLS.
circuits_df = spark.read.csv(f"{raw_folder_path}/circuits.csv")

# COMMAND ----------

# see the data type of the variable.
type(circuits_df)

# COMMAND ----------

# to see the data show() method is going to be use but show by default shows only first 20 records.
circuits_df.show()

# COMMAND ----------

# The above show command output was not well formated and its doing the trucate of the data.
# the databricks provided display command again shows the good results here
display(circuits_df)

# COMMAND ----------

# The header is coming has record data and we need to replace with actual header. The use of the option() will help here
circuits_df = spark.read.option("header" ,True).csv(f"{raw_folder_path}/circuits.csv")

# COMMAND ----------

display(circuits_df)

# COMMAND ----------

# to see the schema structure and what all the default values of the data types are coming here.
circuits_df.printSchema()

# COMMAND ----------

# the describe function use to get the min,max,count,standard deviation , mean, count , this is will give some idea which datatype we can defined.
circuits_df.describe()

# COMMAND ----------

# the above output is just datarame , hence to see it , the show() appended.
circuits_df.describe().show()

# COMMAND ----------

# display is good then show() command.
display(circuits_df.describe())

# COMMAND ----------

# interSchema let dataframe derived the schema based on the data quality.
circuits_df = spark.read.option("header" ,True).option("inferSchema",True).csv(f"{raw_folder_path}/circuits.csv")

# COMMAND ----------

# now see the schema definaion after the inferSchema Option
circuits_df.printSchema()

# COMMAND ----------

# Make the big line into the shorten line , split the code by \
circuits_df = spark.read \
.option("header" ,True) \
.option("inferSchema",True) \
.csv(f"{raw_folder_path}/circuits.csv")

# COMMAND ----------

# The alternative of the interSchema is to make own schema and use while reading it.
# the Struct is required to prepared, For that import Struct
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DoubleType

# COMMAND ----------

# StructField("column_name","datatype",NULL/NOT NULL)
# False is NOT NULL
# True is NULL
# StructType --> represent rows
# StructField --> represent columns
circuits_schema = StructType(fields=[StructField("circuitId", IntegerType(), False),
                                     StructField("circuitRef", StringType(), True),
                                     StructField("name", StringType(), True),
                                     StructField("location", StringType(), True),
                                     StructField("country", StringType(), True),
                                     StructField("lat", DoubleType(), True),
                                     StructField("lng", DoubleType(), True),
                                     StructField("alt", IntegerType(), True),
                                     StructField("url", StringType(), True)
])

# COMMAND ----------

# use the circuits_schema while reading the dataframe from the CSV file.
circuits_df = spark.read \
.option("header" ,True) \
.schema(circuits_schema) \
.csv(f"{raw_folder_path}/circuits.csv")

# COMMAND ----------

display(circuits_df)

# COMMAND ----------

circuits_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 : 4 Different ways to select required and limited columns

# COMMAND ----------

# Way1 plain selected columns , here we cannot rename or apply the alias to the column
circuites_selected_df = circuits_df.select("circuitId","circuitRef","name","location","country","lat","lng","alt")

# COMMAND ----------

display(circuites_selected_df)

# COMMAND ----------

#Way2 to display the column  dataframe.column_name
# here alias is applied.
circuites_selected_df = circuits_df.select(circuits_df.circuitId,circuits_df.circuitRef,circuits_df.name.alias("Name"),circuits_df.location,circuits_df.country,circuits_df.lat,circuits_df.lng,circuits_df.alt)

# COMMAND ----------

display(circuites_selected_df)

# COMMAND ----------

# way 3 dataframe["column_name"]
# here alias is applied.
circuites_selected_df = circuits_df.select(circuits_df["circuitId"],circuits_df["circuitRef"].alias("Circuit Ref"),circuits_df["name"],circuits_df["location"],circuits_df["country"],circuits_df["lat"],circuits_df["lng"],circuits_df["alt"])

# COMMAND ----------

display(circuites_selected_df)

# COMMAND ----------

# way 4  using the function col
# here alias is applied and this is easy way because of the less length.
from pyspark.sql.functions import col
circuites_selected_df = circuits_df.select(col("circuitId"),col("circuitRef"),col("name"),col("location"),col("country").alias("circuit contry"),col("lat"),col("lng"),col("alt"))

# COMMAND ----------

display(circuites_selected_df)

# COMMAND ----------

# this 4th way will be use now going forward.
from pyspark.sql.functions import col
circuites_selected_df = circuits_df.select(col("circuitId"),col("circuitRef"),col("name"),col("location"),col("country"),col("lat"),col("lng"),col("alt"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Rename the column as we need in the final schema

# COMMAND ----------

# The lit function is required to convert the variable in the form of the column
from pyspark.sql.functions import lit
circuites_renamed_df = circuites_selected_df.withColumnRenamed("circuitId","circuit_id") \
.withColumnRenamed("circuitRef","circuit_ref") \
.withColumnRenamed("lat","latitude") \
.withColumnRenamed("lng","longitude") \
.withColumnRenamed("alt","altitude") \
.withColumn("data_source",lit(v_data_source))

# COMMAND ----------

display(circuites_renamed_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4 : Add the new column Ingestion date

# COMMAND ----------

# the extra column is added with name ingestion_date and it holds the current timestamp values.
from pyspark.sql.functions import current_timestamp
#add the new column with full command
#circuites_final_df = circuites_renamed_df.withColumn("ingestion_date",current_timestamp())
#add the new column with function imported
circuites_final_df = add_ingestion_date(circuites_renamed_df)

# COMMAND ----------

display(circuites_final_df)

# COMMAND ----------

# FOR testing purpose , let say name column "LATESH" is added and value for it is "SANGANI"
# the withColumn will fail because "SANGANI" is the value not the column
# to convert value in the form of the column we need the lit function to import
from pyspark.sql.functions import current_timestamp , lit
circuites_final_test = circuites_renamed_df.withColumn("ingestion_date",current_timestamp()).withColumn("LATESH",lit("SANGANI"))

# COMMAND ----------

display(circuites_final_test)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5 : Write the data in the database using the parqut format

# COMMAND ----------

# save the file in the new processed folder location
#circuites_final_df.write.parquet(f"{processed_folder_path}/circuits")
# line 2 is commented because it will fail with multiple rerun.

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/databrickscourcedl/processed/circuits

# COMMAND ----------

# confirm the data is stored well and no formatting is lossed.
df = spark.read.parquet(f"{processed_folder_path}/circuits/*.parquet")

# COMMAND ----------

display(df)

# COMMAND ----------

# Re-running the entire note book fails the write statement has path already present
# add the mode option to overwrite the new existing file
circuites_final_df.write.mode("overwrite").parquet(f"{processed_folder_path}/circuits/")

# COMMAND ----------

# Re-running the entire note book fails the write statement has path already present
# add the mode option to overwrite the new existing file
circuites_final_df.write.mode("overwrite").format("parquet").saveAsTable("processed_db.circuits")

# COMMAND ----------

# confirm the data is stored well and read all the files
df = spark.read.parquet(f"{processed_folder_path}/circuits")

# COMMAND ----------

display(df)

# COMMAND ----------



# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")

# COMMAND ----------

