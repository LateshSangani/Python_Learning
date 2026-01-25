1) Dataframe
2) drop duplicate
3) disticnt
4) withcolumn + withcolumnrename
5) column drop
6) when clause
7) lit, col
8) rename multiple columm names in the dataframe
******************************************************************RDD Code**************************************************************************
from pyspark.rdd import RDD
from pyspark.sql.dataframe import DataFrame

import findspark   
findspark   #  <module 'findspark' from 'C:\\Users\\latesh.sangani\\Anaconda3\\lib\\site-packages\\findspark.py'>
findspark.find()  # 'C:\\Users\\latesh.sangani\\Anaconda3\\lib\\site-packages\\pyspark'  , C:\Programs\spark-3.2.1-bin-hadoop3.2
findspark.init()
sc=SparkContext()  # start the entry point Spark context
a=sc.parallelize([1,2,3,4])
a.collect()  # [1, 2, 3, 4]
type(a)  # pyspark.rdd.RDD
a=sc.parallelize(['latesh','sangani','vaneesa','sangani'])
a.take(1) #['latesh']
a.take(3) #['latesh', 'sangani', 'vaneesa']
sc.stop()  # Stop the spark context
sc=SparkContext() # re-start the Spark context

************************************************************************************************************************************************


****************************************************************Another video**************************************************************************
pyspark commands run over the azure data bricks.
https://www.youtube.com/watch?v=BDy5VEOtmNg&list=PL50mYnndduIGmqjzJ8SDsa9BZoY7cvoeD&index=1

1) %fs ls /Filestore/tables/     -> list all the files present in that path.  fs is file system.
2) emp_json=spark.read.json('/Filestore/tables/emp_json.json') #> read the JSON file in the form of JSON file
3) emp_text=spark.read.text('/Filestore/tables/emp_json.json') #> read the JSON file in the form of text file
4) dispaly(emp_text) -> provide the visible output in the notebook.
5) emp_json.printSchema() -> tell about column ,  datatypes  , null / not null definations of the any created dataframe object.
6) display(emp_json) -> take input any dataframe object like xml,json,csv files and show output in the form of the data frame object created.
7) dbutils.fs.put("/Filestore/tables/Latesh.json","""
{"string":"string1","int":1,"array":[1,2,3],"dict":{"key":"value1"}}
{"string":"string2","int":2,"array":[4,5,6],"dict":{"key":"value2","extra_key":"extra_value3"}}
""",True)

dbutils.fs.put("C:/Users/latesh.sangani/OneDrive - Accenture/Technology/Python/Latesh.json","""
{"first_name":"James", "last_name":"Butterburg", "address": {"street": "6649 N Blue Gum St", "city": "New Orleans","state": "LA", "zip": "70116" }}
{"first_name":"Josephine", "last_name":"Darakjy", "address": {"street": "4 B Blue Ridge Blvd", "city": "Brighton","state": "MI", "zip": "48116" }}
{"first_name":"Art", "last_name":"Chemel", "address": {"street": "8 W Cerritos Ave #54", "city": "Bridgeport","state": "NJ", "zip": "08014" }}
""",True)

#> this will make  the new json file Latesh.json
8) creating temporary view on JSON file
%sql 
CREATE TEMPORARY VIEW latesh_view
USING JSON
OPTIONS(path , "/Filestore/tables/Latesh.json")
9) %sql 
select * from latesh_view
10) latesh_json=spark.read.option("multiline","true").json('/Filestore/tables/Latesh.json')    
#> multiline JSON with many elements are present and all elements cannot fit in the single row.
11) RDD : Resilient Distrubuted Dataset.
my_data = ['{"name":"Latesh","address":{"city":"Banglore","state":"Maharashtra"}]']
my_rdd = sc.parallelize(my_data)
my_df = spark.read.json(my_rdd)
my_df.printSchema()
12) display(my_df.select("address.city","address.state","name"))  -> select the column from the JSON.
13) emp_json.write.mod('append').json('/Filestore/tables/emp_json.json')  -> it will make the new JSON file with some number file name, here emp_json dataframe must exists.
14) emp_json.write.mod('override').json('/Filestore/tables/emp_json.json')  -> it will make the new JSON file and delete old file, here emp_json dataframe must exists.
15) Read and Write excel file.
-> to read excel file download the com.crealytics:spark-excel_2.12:0.13.5 or any latest version into the cluster where we are running the excel file.
-> Clusters -> cluster_name -> Libraries -> Install New -> Maven -> Search Package -> Maven Central (drop down) -> search string "spark-excel"
excel_data=spark.read.format("com.crealytics.spark.excel").option("header","true").option("inferSchema","true").load("/FileStore/tables/myexcel.xlsx")
or
excel_data=spark.read.format("com.crealytics.spark.excel").option("header","true").option("inferSchema","true").load("/FileStore/tables/")
#here if folder has single excel file it will only readup.
16) emp_csv=spark.read.csv('/Filestore/tables/emp_csv.csv')   #> this way CSV file can read.
emp_csv=spark.read.format("csv").option("header","true").option("inferSchema","true").load("/FileStore/tables/emp_csv.csv")  -> alternate way to read CSV file.
#> read csv file and convert into excel file.
17) emp_csv.select("*").write.format("com.crealytics.spark.excel").option("header","true").option("inferSchema","true").save("/Filestore/tables/emp_excel.xlsx",mode="overwrite")
#> new excel file created.
18) emp_csv.select("*").write.format("com.crealytics.spark.excel").option("header","true").option("inferSchema","true").save("/Filestore/tables/excel_folder",mode="overwrite")
#> here file name is not mentioned , so here folder with name excel_folder will be created and new file having same name excel_folder.xlsx will be created.
19) Read and Write the XML file.
-> to read excel file download the com.databricks-spark-xml_2.12 or any latest version into the cluster where we are running the excel file.
-> Clusters -> cluster_name -> Libraries -> Install New -> Maven -> Search Package -> Maven Central (drop down) -> search string "spark.xml"
-> The XML support is not present for the Spark 2.x.x version , support starts from Spark 3.0.0, Scala 2.12
emp_xml=spark.read.format("com.databricks.spark.xml").option("rootTag","emp").option("rowTag","row").load("/Filestore/tables/emp_xml.xml")  -> XML read
emp_xml=spark.read.format("xml").option("rootTag","emp").option("rowTag","row").load("/Filestore/tables/emp_xml.xml") ->alternate way to read XML
rowTag -> The Row tag of the XML file to treat as the Row. default is ROW  4.04
rootTag -> The Row tag of the XML file to treat as the Root. default is ROWS
if we dont specify the rowTag and rootTag option then also the dataframe object will be created but it does not hold any schema 
emp_xml.printSchema()  -> it will just show value "root".
display(emp_xml) -> it will just show value "OK".
20)
custom made Schema of the table.

from pyspark.sql.types import *
customschema=StructType([   \
StructField("COMM",StringType(),True),  \
StructField("DEPTNO",StringType(),True),  \
StructField("EMPNO",StringType(),True),  \
StructField("ENAME",StringType(),True),  \
--
--
StructField("ENAME",StringType(),True)])

just type customschema in the notebook row and see the schema created.
)
21) Just want to see the content of the XML
xml_read = spark.read.text("/Filestore/tables/emp_xml.xml")
display(xml_read)
<emp>  #single combination of the start and end  rootTag
 <row> #multiple rows for number of the employees. rowTag
  <COMM>value1</COMM>
  <DEPTNO>value1</DEPTNO>
  <EMPNO>value1</EMPNO>
  -- --
  -- --
 <row>
 <row>
  <COMM>value2</COMM>
  <DEPTNO>value2</DEPTNO>
  <EMPNO>value2</EMPNO>
  -- --
  -- --
 <row>
</emp>
22) emp_xml=spark.read.format("xml").option("rootTag","emp").option("rowTag","row").load("/Filestore/tables/emp_xml.xml",schema=customschema) 
  without providing the input the customschema , things will also work and but with cutomschema , 
  the required datatypes mentioned on the custom schema will be converted.
23) emp_xml.select("*").write.format("com.databricks.spark.xml").option("rootTag","emp").option("rowTag","row").save("/Filestore/tables/xml_folder",mode="overwrite")   -> will make the new file and mode="append"
#> to do write the dataframe emp_xml must created before.
24) !pip /usr/bin/spark-shell --packages com.databricks:spark-xml_2.12:0.9.0
-> command to install spark XML packages from the cell of the notebook.
25) The databricks has option to the make the jobs and the job can be made of the Notebooks,SET JAR ,Configure Spark-Submit
26) !pip install urllib -> command to install the libraries from the cell of the notebook.
27) import urllib
    urllib.request.urlretrieve("https://resource.lendingclub.com/Loandata_csv.zip","/tmp/Loandata_csv.zip")
 -> downlaod the zip file from the external URL to local path
28) %sh
unzip /tmp/Loandata_csv.zip                          -> in case of the .gz file use "gunzip" command.
tail -n +2 Loandata_csv.csv > temp.csv               -> the file default gets created in the folder /databricks/driver/
rm Loandata_csv.csv
29) see the file present or not.
%fs ls file:/databricks/driver/
30) Move file from the databricks location to user own loaction.
dbutils.fs.mv("file:/databricks/driver/temp.csv","dbfs:/tmp/Loan_CSV.csv")
31) dbutils.fs.ls("dbfs:/tmp/")  #> same as ls command to check the file is present or not.
32) %run ./Custom_Logging   -> this command is used to call existing notebook in the current notebook.


custom logging -> Custom_Logging.py program to catch user made logs 

import logging
import time
import datatime

file_date= datatime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
p_dir = '/tmp/'        # here  the  dbfs:/FileStore/CustomLogging_Folder/ path cannot used , at later stage Python give error. hence option left for tmp path.
p_filename = 'custom_log' + file_date + '.log'
p_logfile = p_dir + p_filename
print(p_logfile)
# logger with custom log
logger = logging.getLogger('custom_log')   # anything can write here, it will come with every line some times we can write log4j
logger.setLevel(logging.DEBUG)
#create file handeller that even handel which logs even debug messages
fh = logging.FileHandler(p_logfile,mode='a')
#create  the consol handeller with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handeller.
formatter = logging.Formatter("%{asctime}% - %{name}% - %{levelname}% - %{message}%")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
#clear old logs information
if (logger.hasHandlers()):
    logger.handlers.clear()
# add handellers to logger
logger.addHandler(fh)
logger.addHandler(ch)


Now call the file Custom_Logging.py file  into new python file  Latesh.py

%run ./Custom_Logging.py
logger.info('** start info logger here **')
logger.debug('** start DEBUG logger here **')
logger.error('** start Error logger here **')
logger.warning('** start Warning logger here **')
logger.Critical('** start Critical logger here **')

o/p: 2022-02-02 12:34:34 - custom_log - INFO - ** start info logger here **
o/p: 2022-02-02 12:34:34 - custom_log - INFO - ** start DEBUG logger here **
o/p: 2022-02-02 12:34:34 - custom_log - INFO - ** start Error logger here **
o/p: 2022-02-02 12:34:34 - custom_log - INFO - ** start Warning logger here **
o/p: 2022-02-02 12:34:34 - custom_log - INFO - ** start Critical logger here **

a=12
b='RAVI'
try:
   c=a+b
    
except Exception as ex:
        logger.error(ex)
logging.shutdown()     

dbutils.fs.mv("file:"+p_logfile , "dbfs:/FileStore/CustomLogging_Folder/"+p_filename)
dbutils.fs.ls("/FileStore/CustomLogging_Folder/")

%sql
DROP TABLE IF EXISTS CUSTOM_LOGGING;
CREATE TABLE IF NOT EXISTS CUSTOM_LOGGING
USING TEXT OPTIONS(path '/FileStore/CustomLogging_Folder/*',header=true)

%sql
select * from CUSTOM_LOGGING;

%sql
REFRESH TABLE CUSTOM_LOGGING
  
