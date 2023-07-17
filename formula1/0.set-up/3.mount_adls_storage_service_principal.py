# Databricks notebook source
# MAGIC %md
# MAGIC ## 1) Register the Azure AD Application/ Service Priniple
# MAGIC ## 2) Generate the seceret/password for the application
# MAGIC ## 3) Set Spark Config with App/Client id , Directory / Tenant Id and Secret
# MAGIC ## 4) Assign Role "Storage Blob Data Contributor" to the Data Lake

# COMMAND ----------

# MAGIC %md
# MAGIC ### values derived from the service principle and storage account name.
# MAGIC ### values are hardcode here but it will copy in the azure keyvault in the future chapter.
# MAGIC ### mapping of the storage account with service principle should be done in advanced before mounting.
# MAGIC ### the mapping done from the IAM of the storage account

# COMMAND ----------

# values derived from the service principle and storage account name.
# values are hardcode here but it will copy in the azure keyvault in the future chapter.
# mapping of the storage account with service principle should be done in advanced before mounting.
# the mapping done from the IAM of the storage account
storage_account_name = "datasourceformula1"
container_name = "demo"
# service principle parameters derived by registering the New Application in the Azure Active Directory
client_id            = "aaa42243-2425-403d-8037-518438780e38"
tenant_id            = "065d03af-dbd9-4135-8ef3-49b240d7eb87"
# Derived after App Registeration is done , new client seceret key generated.
client_secret        = "OWK8Q~aR3Z5jTi2dNLM4iCkecpEwB0_2IXWMTbkh"

# COMMAND ----------

# MAGIC %md
# MAGIC #### Set the Spark Config Parameters

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.datasourceformula1.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.datasourceformula1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.datasourceformula1.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.datasourceformula1.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.datasourceformula1.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net"))
