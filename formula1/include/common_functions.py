# Databricks notebook source
# MAGIC %md
# MAGIC #Inside include/common_functions

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %md
# MAGIC #### Standard Function import

# COMMAND ----------

from pyspark.sql.functions import current_timestamp , col, concat , lit , upper

# COMMAND ----------

# MAGIC %md
# MAGIC #### Function to add new extra column ingestion date at the last of the all the Raw Tables

# COMMAND ----------

from pyspark.sql.functions import current_timestamp
def add_ingestion_date(input_df):
    output_df = input_df.withColumn("ingestion_date",current_timestamp())
    return output_df


# COMMAND ----------

# MAGIC %md
# MAGIC #### Function to arrange all the columns in such form ,so that partition column will append at last

# COMMAND ----------

def append_column(input_df,partition_id):
    columns_list = []
    for column_name in input_df.schema.names:
        print(column_name)
        if column_name != partition_id:
            columns_list.append(column_name)
        else:
            print ("dont add partition column here")
    # outside of the loop , add the last partition column    
    columns_list.append(partition_id)  
    output_df = input_df.select(columns_list)
    return output_df


# COMMAND ----------

# MAGIC %md
# MAGIC #### DATALAKE : Function to Overwrite the data for the input dataframe in the Destination DB using partition_id

# COMMAND ----------

def overwrite_partition_data(input_df,input_db,input_table,partition_id):
    output_df = append_column(input_df,partition_id)
    spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
    if (spark._jsparkSession.catalog().tableExists(f"{input_db}.{input_table}")):
        output_df.write.mode("overwrite").insertInto(f"{input_db}.{input_table}")
    else:
        output_df.write.mode("overwrite").partitionBy(f"{partition_id}").format("parquet").saveAsTable(f"{input_db}.{input_table}")
    return output_df

# COMMAND ----------

# MAGIC %md
# MAGIC #### Function to convert the column values in the list

# COMMAND ----------

def column_to_list(input_df,table_column_name):
    df_row_list = input_df.select(table_column_name) \
                          .distinct() \
                          .collect()
    columns_list = [row[table_column_name] for row in df_row_list]
    return columns_list

# COMMAND ----------

# MAGIC %md
# MAGIC #### DELTALAKE : Function to Overwrite the data for the input dataframe in the Destination DB using partition_id

# COMMAND ----------

def merge_delta_data(input_df,input_db,input_table,container_path,partition_id,primary_key):
    # The join on the Primary Key Is enough , but performance wise its slow because Databricks does not know in which partition the Primary key is present , 
    # hence the scanning of the all the partition will be performed by the databricks. 
    # To avoid of the scanning the EXTRA join of the partition column is required , this will boost the performance.
    #
    # Means use the join condition column to find the dynamic partition insted of the hardcoding search of the partition ex: race_id = 1234
    spark.conf.set("spark.databricks.optimizer.dynamicPartitionPruning","true") 
    from delta.tables import DeltaTable
    if (spark._jsparkSession.catalog().tableExists(f"{input_db}.{input_table}")):
        deltaTable = DeltaTable.forPath(spark,f"{container_path}/{input_table}/")
        deltaTable.alias("target").merge(input_df.alias("source"), \
                                         f"target.{primary_key} = source.{primary_key} AND target.{partition_id} = source.{partition_id}") \
        .whenMatchedUpdateAll() \
        .whenNotMatchedInsertAll() \
        .execute()
    else:
        input_df.write.mode("overwrite").partitionBy(f"{partition_id}").format("delta").saveAsTable(f"{input_db}.{input_table}")

# COMMAND ----------


