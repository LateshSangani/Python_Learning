# Databricks notebook source
# MAGIC %md
# MAGIC ### Access the Azure Gen2 storage account using the credentail passthrough in the edit section of the cluster

# COMMAND ----------

# MAGIC %md
# MAGIC ### Steps
# MAGIC #### 1) Edit the spark cluster config ->  fs.azure.account.key.datasourceformula1.dfs.core.windows.net
# MAGIC ##### Enable  credential passthrough for user-level data access
# MAGIC #### 2) List files from the demo container
# MAGIC #### 3) Read data from circuits.csv

# COMMAND ----------

# MAGIC %md
# MAGIC ### The Enable credential passthrough for user-level data access still not provide the access to storage account even the both storage account and database account made by same id and under the same subscription.
# MAGIC ### The contributor Role is required to provide from the IAM section of the Azure Gen2 storage account

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Syntax : dbutils.fs.ls("abfss://container_name@storage_account_name.dfs.core.windows.net")

# COMMAND ----------

dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net")

# COMMAND ----------

df = spark.read.csv("abfss://demo@datasourceformula1.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

df.display()

# COMMAND ----------


