# Databricks notebook source
# MAGIC %md
# MAGIC ## Load the initial configuration

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %run "../include/common_functions"

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Load All the Widgets

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
# the default value is 2099-01-01  , but it can be anything we defined.
dbutils.widgets.text("p_as_of_date","2099-01-01")
v_as_of_date = dbutils.widgets.get("p_as_of_date")
display(v_as_of_date)

# COMMAND ----------

# MAGIC %md
# MAGIC # Import the functions

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import desc , rank , sum , when , count  ,col , asc

# COMMAND ----------

# MAGIC %md
# MAGIC # Read and merge of the data with 2 different ways
# MAGIC ### Approch 1 (DAY1 Only): with all the years in the single dataframe without any list ex: data from 1950 to 2023 Year
# MAGIC ### Approch 2 (DAY 1..n): Here scenario is with in same 2023 year , we get data of the another new races as year is NOT OVER yet i.e new race_id data comes for the new as_of_date and all the calculation done for the same year Day1 data becomes wrong.
# MAGIC ### With LIST of the years input to the data frame , It will read only the new year of the partition and do only for that partition all the re-calculations

# COMMAND ----------

# MAGIC %md
# MAGIC ### Approch 1 : with all the years in the single dataframe without any list

# COMMAND ----------

# MAGIC %md
# MAGIC #------------------------------READ-----------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC #### Read the Input Presentation Data

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain Python

# COMMAND ----------

#input_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Data Lake

# COMMAND ----------

#input_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Delta Lake

# COMMAND ----------

input_df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC #------------------------------MERGE-----------------------------------

# COMMAND ----------

# MAGIC %md 
# MAGIC ### first group the data

# COMMAND ----------

#dashboard_grouped_df = input_df \
#.groupBy("race_year","driver_name","driver_nationality","team") \
#.agg(sum("points").alias("TotalPoints"))    
#display(dashboard_grouped_df)   

# COMMAND ----------

# Extra Expected wins column added
#dashboard_grouped_df = input_df \
#.groupBy("race_year","driver_name","driver_nationality","team") \
#.agg(sum("points").alias("TotalPoints"),
#     count(when(col("position") == 1,True)).alias("wins"))
#display(dashboard_grouped_df)   

# COMMAND ----------

# MAGIC %md
# MAGIC ### second test the data

# COMMAND ----------

#dashboard_grouped_df.filter("race_year = 2020").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### third apply the window for the Rank

# COMMAND ----------

# Setup the varaible for the windowing function
#
#driver_rank_spec = Window.partitionBy("race_year").orderBy(desc("TotalPoints"),desc("wins"))
#
# Pass the variable input to the rank().over() clause
#
#final_df = dashboard_grouped_df.withColumn("rank",rank().over(driver_rank_spec))
#final_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Approch 2 : with LIST of the years input to the data frame

# COMMAND ----------

# MAGIC %md
# MAGIC ### First prepare the List for the Years ( pre-requsite)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### First get the list of the race year for the new delta AS_OF_DATE data, as data is being analysed based on the race year. 
# MAGIC ##### Why because the aggregation is done based on the race year.
# MAGIC ##### the Aggregation should not repeate for the race_year which already passed.
# MAGIC ##### As the PAST year data will not change anytime in the future.

# COMMAND ----------

# MAGIC %md
# MAGIC #### LOGIC for the LIST POPULATION
# MAGIC ##### load the list of all the years data in the new empty list
# MAGIC ##### For the first time laod when we will history of all the past data this list is required.
# MAGIC ##### For the further AS_OF_DATE we can get the same year data many times
# MAGIC ##### that same year data need to re-calculate every time

# COMMAND ----------

# MAGIC %md
# MAGIC #### Plain Python Way

# COMMAND ----------

#race_years = spark.read.parquet(f"{presentation_folder_path}/dashboard_results") \
#.filter(f" as_of_date = '{v_as_of_date}' ") \
#.select("race_year") \
#.distinct() \
#.collect()
#race_years_list = []
#for i in race_years:
#    race_years_list.append(i.race_year)
#print(race_years_list)

# COMMAND ----------

# MAGIC %md
# MAGIC #### DATA Lake Way

# COMMAND ----------

#race_years = spark.read.parquet(f"{presentation_folder_path}/dashboard_results") \
#.filter(f" as_of_date = '{v_as_of_date}' ") \
#.select("race_year") \
#.distinct() \
#.collect()
#race_years_list = []
#for i in race_years:
#    race_years_list.append(i.race_year)
#print(race_years_list)

# COMMAND ----------

# MAGIC %md
# MAGIC #### DELTA Lake Way

# COMMAND ----------

race_years = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_results") \
.filter(f" as_of_date = '{v_as_of_date}' ") \
.select("race_year") \
.distinct() \
.collect()
race_years_list = []
for i in race_years:
    race_years_list.append(i.race_year)
print(race_years_list)

# COMMAND ----------

type(race_years)

# COMMAND ----------

type(race_years_list)

# COMMAND ----------

# MAGIC %md
# MAGIC #------------------------------READ-----------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC #### Read the Input Presentation Data

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain Python

# COMMAND ----------

#input_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results") \
#    .filter(col("race_year").isin(race_years_list))

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Data Lake

# COMMAND ----------

#input_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")  \
#    .filter(col("race_year").isin(race_years_list))

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Delta Lake

# COMMAND ----------

input_df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_results") \
.filter(col("race_year").isin(race_years_list))

# COMMAND ----------

# MAGIC %md
# MAGIC #------------------------------MERGE-----------------------------------

# COMMAND ----------

# MAGIC %md 
# MAGIC ### first group the data

# COMMAND ----------

dashboard_grouped_df = input_df \
.groupBy("race_year","driver_name","driver_nationality") \
.agg(sum("points").alias("total_points"),
     count(when(col("position") == 1 , True)).alias("wins") )

# COMMAND ----------

# MAGIC %md
# MAGIC ### second test the data

# COMMAND ----------

# test the output  with single year
dashboard_grouped_df.filter("race_year = 2020").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### third apply the window for the Rank

# COMMAND ----------

driver_rank_spec = Window.partitionBy("race_year").orderBy(desc("total_points"),desc("wins"))
final_df = dashboard_grouped_df.withColumn("rank",rank().over(driver_rank_spec))
final_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #------------------------------WRITE-----------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC # Write the results for the future reference and apply all the filteration and analysis

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python but no table creation

# COMMAND ----------

# full load with file creation.
#
# final_df.write.mode("overwrite").partitionBy('race_year').parquet(f"{presentation_folder_path}/dashboard_standings")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Data Lake + Table Creation

# COMMAND ----------

# Write the output of the presentation_db data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as presentation_db used the mounted path
# full load with table and file creation.
#
#final_df.write.mode("overwrite").partitionBy('race_year').format("parquet").saveAsTable("presentation_db.dashboard_standings")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Delta Lake + Table Creation 

# COMMAND ----------

# Write the output of the presentation_db data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as presentation_db used the mounted path
# full load with table and file creation.
#
# final_df.write.mode("overwrite").partitionBy('race_year').format("delta").saveAsTable("presentation_db.dashboard_standings")

# COMMAND ----------

# MAGIC %md
# MAGIC ## READ the Solution 1 and Solution 2 from the "injection/5.ingest_results_file.json"
# MAGIC ## Here Solution 2 with function is implemented

# COMMAND ----------

# its fine not to capture the output dataframe becuase function has wrote now the data and now output dataframe has no use.
#
# overwrite_partition_data(final_df,'presentation_db','dashboard_standings','race_year')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 3 (Delta Lake): Incremental laod ( overwrite ) Complex but Fast Performance (USE DELTA)
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

input_db="presentation_db"
input_table="dashboard_standings"
partition_id="race_year"
primary_key="target.driver_name = source.driver_name AND target.race_year = source.race_year"
merge_delta_data(final_df,input_db,input_table,presentation_folder_path,partition_id,primary_key)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain SQL Read

# COMMAND ----------

# MAGIC %sql
# MAGIC select  race_year,count(*) from presentation_db.dashboard_standings group by race_year;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain Python read

# COMMAND ----------

#df = spark.read.parquet(f"{presentation_folder_path}/dashboard_standings")
#df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

# df = spark.read.parquet(f"{presentation_folder_path}/dashboard_standings")
# df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# test and confirm the data is stored in the readble format
df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_standings/")
df.display()

# COMMAND ----------


