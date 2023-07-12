# Databricks notebook source
# both run cannot be run in the single cell else it will give the error.
# Even comments also not allowed in the run

# COMMAND ----------

# MAGIC %run "/formula1/include/configuration"

# COMMAND ----------

# MAGIC %run "/formula1/include/common_functions"

# COMMAND ----------

races_df = spark.read.parquet(f"{processed_folder_path}/races")

# COMMAND ----------

display(races_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Three Diffrent ways to do the Filter or Where. both keyword are Alias.

# COMMAND ----------

# way 1 : SQL based 
# sql has AND OR keywaords
races_df_filtered = races_df.filter("race_year = 2009 and round <= 5")
races_df_filtered.count()
races_df_filtered = races_df.where("race_year = 2009 and round <= 5")
races_df_filtered.count()

# COMMAND ----------

# way 2 : Python Based
# Python has & | symbol
races_df_filtered = races_df.filter((races_df["race_year"] == "2009") & (races_df["round"] <= 5))
races_df_filtered.count()
races_df_filtered = races_df.where((races_df["race_year"] == "2009") & (races_df["round"] <= 5))
races_df_filtered.count()

# COMMAND ----------

# way 3 : Alternate Python based
# Python has & | symbol
races_df_filtered = races_df.filter((races_df.race_year == "2009") & (races_df.round <= 5))
races_df_filtered.count()
races_df_filtered = races_df.where((races_df.race_year == "2009") & (races_df.round <= 5))
races_df_filtered.count()

# COMMAND ----------

