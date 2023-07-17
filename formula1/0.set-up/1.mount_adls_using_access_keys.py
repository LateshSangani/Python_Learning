# Databricks notebook source
# MAGIC %md
# MAGIC ### Access the Azure Gen2 storage account using the access keys

# COMMAND ----------

# MAGIC %md
# MAGIC ### Steps
# MAGIC #### 1) Setup the spark config fs.azure.account.key
# MAGIC #### 2) List files from the demo container
# MAGIC #### 3) Read data from circuits.csv

# COMMAND ----------

# MAGIC %md
# MAGIC ### It Provide the access of the entire storage account for the read and write. The control of the data access is missing

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Syntax :  spark.conf.set("fs.azure.account.key.storage_account_name.dfs.core.windows.net","Gen 2 storage account key")

# COMMAND ----------

spark.conf.set("fs.azure.account.key.datasourceformula1.dfs.core.windows.net",
               "MaQX8sF00ETsqMcnTGVX7ziHq4/IokY6wZ761bqaKOSARxZEfA82elBtFEYbZfRqPPSGZcs3RFPu+AStZ52cgA==")

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


