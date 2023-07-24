# Databricks notebook source
# MAGIC %md
# MAGIC ### Access the Azure Gen2 storage account using the SAS (Shared Access Keys)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Steps
# MAGIC #### 1) Setup the spark config SAS Token
# MAGIC #### 2) List files from the demo container
# MAGIC #### 3) Read data from circuits.csv

# COMMAND ----------

# MAGIC %md
# MAGIC ### SAS key provide the limited access to the storage account and some controls are present in it
# MAGIC ### Let say READ And LIST access to only "demo" container and for that container only SAS keys generated.
# MAGIC ### also the access set for the limited time duration only

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Syntax : 
# MAGIC ###### spark.conf.set("fs.azure.account.auth.type.storage-account.dfs.core.windows.net", "SAS")
# MAGIC ###### spark.conf.set("fs.azure.sas.token.provider.type.storage-account.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
# MAGIC ###### spark.conf.set("fs.azure.sas.fixed.token.storage-account.dfs.core.windows.net","sas-token-key")

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.datasourceformula1.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.datasourceformula1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.datasourceformula1.dfs.core.windows.net","sp=rl&st=2023-07-12T13:55:47Z&se=2024-11-29T21:55:47Z&spr=https&sv=2022-11-02&sr=c&sig=GEQ8c3LMks9N0FKfaBJFKBSpzpdzFtOTlzSDbt8XtvM%3D")

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Syntax : dbutils.fs.ls("abfss://container_name@storage_account_name.dfs.core.windows.net")

# COMMAND ----------

dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net")

# COMMAND ----------

df = spark.read.csv("abfss://demo@datasourceformula1.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

df.display()
