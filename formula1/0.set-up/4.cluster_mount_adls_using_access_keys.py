# Databricks notebook source
# MAGIC %md
# MAGIC ### Access the Azure Gen2 storage account using the access keys stored in the cluster

# COMMAND ----------

# MAGIC %md
# MAGIC ### Steps
# MAGIC #### 1) Edit the spark cluster config ->  fs.azure.account.key.datasourceformula1.dfs.core.windows.net
# MAGIC ##### add line , the key used here is the access key of the storage account
# MAGIC fs.azure.account.key.datasourceformula1.dfs.core.windows.net MaQX8sF00ETsqMcnTGVX7ziHq4/IokY6wZ761bqaKOSARxZEfA82elBtFEYbZfRqPPSGZcs3RFPu+AStZ52cgA==
# MAGIC #### 2) List files from the demo container
# MAGIC #### 3) Read data from circuits.csv

# COMMAND ----------

# MAGIC %md
# MAGIC ### It Provide the access of the entire storage account at cluster level and now all the notebooks mapped to same cluster will access the storage account.

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Syntax : dbutils.fs.ls("abfss://container_name@storage_account_name.dfs.core.windows.net")

# COMMAND ----------

dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net")

# COMMAND ----------

df = spark.read.csv("abfss://demo@datasourceformula1.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

df.display()
