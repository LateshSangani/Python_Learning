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

races_df = spark.read.parquet(f"{processed_folder_path}/races")

# COMMAND ----------

display(races_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Three Diffrent ways to do the Filter or Where. both keyword are Alias.

# COMMAND ----------

# MAGIC %md
# MAGIC ###### SQL Based

# COMMAND ----------

# way 1 : SQL based 
# sql has AND OR keywaords
races_df_filtered = races_df.filter("race_year = 2009 and round <= 5")
races_df_filtered.count()
races_df_filtered = races_df.where("race_year = 2009 and round <= 5")
races_df_filtered.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Python Based

# COMMAND ----------

# way 2 : Python Based
# Python has & | symbol
races_df_filtered = races_df.filter((races_df["race_year"] == "2009") & (races_df["round"] <= 5))
races_df_filtered.count()
races_df_filtered = races_df.where((races_df.race_year == "2009") & (races_df.round <= 5))
races_df_filtered.count()

# COMMAND ----------

# way 3 : Alternate Python based
# Python has & | symbol
races_df_filtered = races_df.filter((races_df.race_year == "2009") & (races_df.round <= 5))
races_df_filtered.count()
races_df_filtered = races_df.where((races_df.race_year == "2009") & (races_df.round <= 5))
races_df_filtered.count()

# COMMAND ----------


