# Databricks notebook source
# MAGIC %md
# MAGIC ## PRODUCTION READY CODE Solution with Databricks Seceret Scope and Azure Key Vault 
# MAGIC ## And Lastly Mounting and Unmounting of the Storage Accounts

# COMMAND ----------

# MAGIC %md
# MAGIC #### Explore utiities for the seceret to see all the methods it supports.

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

# MAGIC %md
# MAGIC #Steps to make the credential scope is mentioed in the Notes of the databricks

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

# input is the name of the seceret scope made from https://adb-993395267027032.12.azuredatabricks.net/?o=993395267027032#secrets/createScope
dbutils.secrets.list("databrickscource-secret-scope")

# COMMAND ----------

# get the single key value of the scope , the secret value will be hidden
dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-storage-access-key")

# COMMAND ----------

# get the single key value of the scope , the secret value will be hidden
dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-storage-sas-key")

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

# MAGIC %md
# MAGIC #### Explore DBFS (Databricks File System ) utiities 
# MAGIC
# MAGIC ####Benifites of the Databricks Mount:
# MAGIC ####1) Access data without required credentials
# MAGIC ####2) Access files without using the file semantices rather than long storage URL
# MAGIC ####3) Store file to the Object Storage ( ex: Azure BLOB) , so that all the benifites of the Azure get it. 

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

# MAGIC %md
# MAGIC #### To see the default FileStore location , Open the Admin Setting -> Workspace Settings -> Search DBFS string -> Enable DBFS File Browser

# COMMAND ----------

dbutils.fs.ls('/FileStore/')

# COMMAND ----------

display(spark.read.csv('/FileStore/circuits.csv'))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Way 1 : Using the Azure Storage Account Access Key stored in the key-vault and key retrived using databricks seceret scope ( Local To Notebook and No Mounting)

# COMMAND ----------

adls_access_key = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-storage-access-key")

# COMMAND ----------

spark.conf.set("fs.azure.account.key.datasourceformula1.dfs.core.windows.net",adls_access_key)

# COMMAND ----------

dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net")

# COMMAND ----------

df = spark.read.csv("abfss://demo@datasourceformula1.dfs.core.windows.net/circuits.csv")

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Way 2 : Using the Azure Storage SAS Access Key stored in the key-vault and key retrived using databricks seceret scope ( Local To Notebook and No Mounting)

# COMMAND ----------

adls_sas_key = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-storage-sas-key")

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.datasourceformula1.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.datasourceformula1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.datasourceformula1.dfs.core.windows.net",adls_sas_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@datasourceformula1.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Way 3 : Using the Azure Storage Service Priciple Key's stored in the key-vault and key retrived using databricks seceret scope ( Local To Notebook and No Mounting)

# COMMAND ----------

for i in dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-secret"):
    print(i)

# COMMAND ----------

# values derived from the service principle and storage account name.
# values are hardcode here but it will copy in the azure keyvault in the future chapter.
# mapping of the storage account with service principle should be done in advanced before mounting.
# the mapping done from the IAM of the storage account
storage_account_name = "datasourceformula1"
client_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-id")
tenant_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-tenant-id")
client_secret        = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-secret")

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.datasourceformula1.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.datasourceformula1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.datasourceformula1.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.datasourceformula1.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.datasourceformula1.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@datasourceformula1.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Way 4 : Using the Azure Storage Access Key's stored in the key-vault and key retrived using databricks seceret scope (  Cluster Level and and No Mounting)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### edit the cluster and in the advance opttion write
# MAGIC ##### Syntax : 
# MAGIC     #### fs.azure.account.key.datasourceformula1.dfs.core.windows.net {{secrets/secret-scope-name/seceret-name}}
# MAGIC ##### Ex:
# MAGIC     #### fs.azure.account.key.datasourceformula1.dfs.core.windows.net {{secrets/databrickscource-secret-scope/databricks-storage-access-key}}

# COMMAND ----------

# MAGIC %md
# MAGIC ##### now without spark config setup at cluster level values are defined and now same can give the direct acccess to the storage account

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@datasourceformula1.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@datasourceformula1.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### FINAL : Using the Azure Storage Service Principle values stored in key-vault and key retrived using databricks seceret scope Notebook level and Data can be mount and unmount to storage account.
# MAGIC ### MOUNT And UNMOUNT real need of the project as the local DBFS storage gets deleted if workspace gets deleted.
# MAGIC ### The Actual Data is required in the storage account and data will be seperate from the Databricks

# COMMAND ----------

# values derived from the service principle and storage account name.
# values are hardcode here but it will copy in the azure keyvault in the future chapter.
# mapping of the storage account with service principle should be done in advanced before mounting.
# the mapping done from the IAM of the storage account
storage_account_name = "datasourceformula1"
client_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-id")
tenant_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-tenant-id")
client_secret        = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-secret")

# COMMAND ----------

#  Set the Distionary for the Mount function holding the same spark config information
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ## MOUNT Example

# COMMAND ----------

# mount demo folder 
container_name = "demo"
dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ## UNMOUNT Example

# COMMAND ----------

dbutils.fs.unmount(f"/mnt/{storage_account_name}/demo")

# COMMAND ----------

# MAGIC %md
# MAGIC # BEST
# MAGIC ### MOUNT FUNCTIONS to MAKE LIFE Easy

# COMMAND ----------

# in real project , where many folders need to mount the function is getting prepared which takes the input contrainer name and storage account name. it will check its the container which is planning to mount if already exist. if yes then delete the mount and make new mount
def mount_adls(storage_account_name,container_name):
    #storage_account_name = "datasourceformula1"
    client_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-id")
    tenant_id            = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-tenant-id")
    client_secret        = dbutils.secrets.get(scope="databrickscource-secret-scope" , key="databricks-client-secret")

    configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
    
    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{container_name}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_account_name}/{container_name}")

    # use the mount function to inside the custimaized function
    dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

# check the list of the all the mounts before run
dbutils.fs.mounts()

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/datasourceformula1/raw")

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/datasourceformula1/processed")

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/datasourceformula1/presentation")

# COMMAND ----------

# unmount old folders which were mount in the file mount_adls_storage.py
dbutils.fs.unmount("/mnt/datasourceformula1/demo")

# COMMAND ----------

mount_adls("datasourceformula1","raw")

# COMMAND ----------

mount_adls("datasourceformula1","processed")

# COMMAND ----------

mount_adls("datasourceformula1","presentation")

# COMMAND ----------

mount_adls("datasourceformula1","demo")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/datasourceformula1/raw")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/datasourceformula1/processed")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/datasourceformula1/presentation")

# COMMAND ----------

# test the mount point is ready
dbutils.fs.ls("/mnt/datasourceformula1/demo")

# COMMAND ----------

# check the list of the all the mounts after run
dbutils.fs.mounts()

# COMMAND ----------


