# Databricks notebook source
# Databricks notebook source vairable for the mount point connection.
# values derived from the service principle and storage account name.
# values are hardcode here but it will copy in the azure keyvault in the future chapter.
# mapping of the storage account with service principle should be done in advanced before mounting.
# the mapping done from the IAM of the storage account
storage_account_name = "databrickscourcedl"
# service principle parameters
client_id            = "2105c081-d8bf-43e2-b120-2aced3c763ea"
tenant_id            = "929c66f7-f159-487b-9c74-168b37f38962"
client_secret        = "kog8Q~pN9NykgT1noRSOImsBrXiGqD.aBLTlxbmG"

# COMMAND ----------

#  here the configs variable prepared and used in the 3rd cell for the mount command.

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

# mount raw folder 

container_name = "raw"
dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/databrickscourcedl/raw")

# COMMAND ----------

# check the list of the all the mounts
dbutils.fs.mounts()

# COMMAND ----------

# mount processed folder 
container_name = "processed"
dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

# in real project , where many folders need to mount the function is getting prepared which takes the input contrainer name.
def mount_adls(container_name):
    dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

mount_adls("processed")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/databrickscourcedl/processed")

# COMMAND ----------

# check the list of the all the mounts
dbutils.fs.mounts()

# COMMAND ----------

