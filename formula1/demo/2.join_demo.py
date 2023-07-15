# Databricks notebook source
# MAGIC %md
# MAGIC ## Pre-requsit : all the injection files should be laoded and data stored in the processed folder

# COMMAND ----------

# MAGIC %md
# MAGIC # Load Run time configuration

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %run "../include/common_functions"

# COMMAND ----------

# MAGIC %md
# MAGIC # Prepare the Join Dataframes

# COMMAND ----------

# Two DF join with filter condition , rename of the same column name in the same DataFrame , 
circuites_df = spark.read.parquet(f"{processed_folder_path}/circuits").where("circuit_id < 79").withColumnRenamed("name","circuit_name")
races_df = spark.read.parquet(f"{processed_folder_path}/races").filter("race_year = 2019").withColumnRenamed("name","race_name")

# COMMAND ----------

# By default the JOIN condition is the inner
# If we dont pass the third parameter , the join function will consider the default value as inner
# Here the combine output of the both dataframe is coming and circuit_id gets duplicated
# == is written as its Python code
races_circuites_df = circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"inner" )
# another way to display the output.
races_circuites_df.display()

# COMMAND ----------

# If data is not requried to store , just want to see it then show() or display() will also help
circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"inner" ) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country , races_df.race_name , races_df.round).display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Inner Join

# COMMAND ----------

# here data is stored in the data frame and later display
races_circuites_df = circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"inner" ) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country , races_df.race_name , races_df.round)
races_circuites_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC # Left Outer Join

# COMMAND ----------

# Left DF : circuites_df
# Right DF : races_df
races_circuites_df = circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"left" ) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country , races_df.race_name , races_df.round)
display(races_circuites_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Right Outter Join

# COMMAND ----------

# Left DF : circuites_df
# Right DF : races_df
races_circuites_df = circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"right" ) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country , races_df.race_name , races_df.round)
display(races_circuites_df)

# COMMAND ----------

# MAGIC %md 
# MAGIC # Full Outer Join

# COMMAND ----------

# Left DF : circuites_df
# Right DF : races_df
races_circuites_df = circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"full" ) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country , races_df.race_name , races_df.round)
display(races_circuites_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Cross Join
# MAGIC #### keyword crossJoin

# COMMAND ----------

# without any join condition
# keyword crossJoin
# Left DF : circuites_df
# Right DF : races_df
races_circuites_df = circuites_df.crossJoin(races_df) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country , races_df.race_name , races_df.round  )
display(races_circuites_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Semi Join  
# MAGIC ##### its inner join + all the MATCHED data of left DF + all the columns of the left DF OUTPUT

# COMMAND ----------

# The SEMI join is same as INNER join, Means common record of the both tables will come. but it will provide only the output columns of the Left Dataframe
# Here data is filter and column is filtered.
# The reference of the right dataframe races_df.race_name , races_df.round will throw the error  , hence its removed
# If .select(circuites_df.circuit_name , circuites_df.location , circuites_df.country ) removed then all the column of LEFT table comes up.
# Left DF : circuites_df
# Right DF : races_df
races_circuites_df = circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"semi" ) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country )
display(races_circuites_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Anti Join
# MAGIC ##### its inner join + all NON MATCH data of left DF + all the columns of the left DF OUTPUT

# COMMAND ----------

# The ANIT join provide every thing on the LEFT data frame not found in the Right Data frame , means left over data of the non join records
# Here data is filter and column is filtered.
# The reference of the right dataframe races_df.race_name , races_df.round will throw the error  , hence its removed
# If .select(circuites_df.circuit_name , circuites_df.location , circuites_df.country ) removed then all the column of LEFT table comes up.
# Left DF : circuites_df
# Right DF : races_df
races_circuites_df = circuites_df.join(races_df,circuites_df.circuit_id == races_df.circuit_id,"anti" ) \
.select(circuites_df.circuit_name , circuites_df.location , circuites_df.country  )
display(races_circuites_df)

# COMMAND ----------


