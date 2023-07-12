# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

# Accept the input the secret made from the datascripts home page : https://adb-2643165434444923.3.azuredatabricks.net/?o=2643165434444923#secrets/createScope
dbutils.secrets.list("databrickscource-secret-scope")

# COMMAND ----------

# get the single key value of the scope , the secret value will be hidden
dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-id")

# COMMAND ----------

# get the single key value of the scope , the secret value will be hidden
dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-tenant-id")

# COMMAND ----------

# get the single key value of the scope , the secret value will be hidden
dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-secret")

# COMMAND ----------

for i in dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-secret"):
    print(i)

# COMMAND ----------

# Databricks notebook source vairable for the mount point connection.
# values derived from the service principle and storage account name.
# values are hardcode here but it will copy in the azure keyvault in the future chapter.
# mapping of the storage account with service principle should be done in advanced before mounting.
# the mapping done from the IAM of the storage account
storage_account_name = "databrickscourcedl"
client_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-id")
tenant_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-tenant-id")
client_secret        = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-secret")

# COMMAND ----------

#  here the configs variable prepared and used in the 3rd cell for the mount command.

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

# in real project , where many folders need to mount the function is getting prepared which takes the input contrainer name.
def mount_adls(container_name):
    dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

# check the list of the all the mounts
dbutils.fs.mounts()

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/databrickscourcedl/raw")

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/databrickscourcedl/processed")

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/databrickscourcedl/presentation")

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/databrickscourcedl/demo")

# COMMAND ----------

mount_adls("raw")

# COMMAND ----------

mount_adls("processed")

# COMMAND ----------

mount_adls("presentation")

# COMMAND ----------

mount_adls("demo")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/databrickscourcedl/raw")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/databrickscourcedl/processed")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/databrickscourcedl/presentation")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/databrickscourcedl/demo")

# COMMAND ----------

# check the list of the all the mounts
dbutils.fs.mounts()

# COMMAND ----------

