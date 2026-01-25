The juyper notbook will open the default path :  C:\Users\Lenovo
The below full code is present in the file Pandas.ipynb of same path : 
C:\Users\Lenovo\OneDrive\Technology\Python\Jupyter_Project

Pandas libarary used for the data manapulation, analysis  cleaning and for the Python code.
Pandas are the open source Python Package. read datas from many formates , Fast and memory efficient. 
The standard Python Data Wrangling Library.


Three diffrent ways to insatalled the Python.

1) Installed pandas via command prompt 

C:\Users\Lenovo>pip install pandas
Collecting pandas
  Using cached pandas-1.3.5-cp310-cp310-win_amd64.whl (10.2 MB)
Requirement already satisfied: python-dateutil>=2.7.3 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from pandas) (2.8.2)
Requirement already satisfied: numpy>=1.21.0 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from pandas) (1.21.4)
Requirement already satisfied: pytz>=2017.3 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from pandas) (2021.3)
Requirement already satisfied: six>=1.5 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from python-dateutil>=2.7.3->pandas) (1.16.0)
Installing collected packages: pandas
Successfully installed pandas-1.3.5

C:\Users\Lenovo>pip3 install pandas
Requirement already satisfied: pandas in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (1.3.5)
Requirement already satisfied: numpy>=1.21.0 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from pandas) (1.21.4)
Requirement already satisfied: python-dateutil>=2.7.3 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from pandas) (2.8.2)
Requirement already satisfied: pytz>=2017.3 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from pandas) (2021.3)
Requirement already satisfied: six>=1.5 in c:\users\latesh.sangani\appdata\local\programs\python\python310\lib\site-packages (from python-dateutil>=2.7.3->pandas) (1.16.0)

C:\Users\Lenovo>pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.9.3-cp310-cp310-win_amd64.whl (1.2 MB)
Installing collected packages: psycopg2
Successfully installed psycopg2-2.9.3

2) Installed pandas in the PyCharm.

Files -> settings -> Project:PyCharm_Project -> Python Interpreter -> Click + -> search pandas -> click intall and close the popup.

3) Installed pandas via Anaconda Prompt.

Open the Anaconda command prompt.
run the below command.

(base) C:\Users\Lenovo>conda install pandas
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\latesh.sangani\Anaconda3

  added / updated specs:
    - pandas


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-4.11.0               |   py39haa95532_0        14.4 MB
    ------------------------------------------------------------
                                           Total:        14.4 MB

The following packages will be UPDATED:

  conda                               4.10.3-py39haa95532_0 --> 4.11.0-py39haa95532_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-4.11.0         | 14.4 MB   | ################################################################################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(base) C:\Users\Lenovo>

(base) C:\Users\latesh.sangani>conda install psycopg2
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\Lenovo\Anaconda3

  added / updated specs:
    - psycopg2


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    libpq-12.9                 |       hb652d5d_1         2.7 MB
    psycopg2-2.8.6             |   py39hcd4344a_1         156 KB
    ------------------------------------------------------------
                                           Total:         2.9 MB

The following NEW packages will be INSTALLED:

  libpq              pkgs/main/win-64::libpq-12.9-hb652d5d_1
  psycopg2           pkgs/main/win-64::psycopg2-2.8.6-py39hcd4344a_1


Proceed ([y]/n)? y


Downloading and Extracting Packages
libpq-12.9           | 2.7 MB    | ############################################################################ | 100%
psycopg2-2.8.6       | 156 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(base) C:\Users\latesh.sangani>



#Dataframes are the 2 dimensional data sets in the form of the rows and columns 
#and its used to collect data and later do manipulation.
#Series is the 1 dimensional array capable to store any kind of the data int,float , str. 
#Its just simply columns of the table or excel sheet.


#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Syntax:
pd.Series(data=None, index=None, dtype=None, name=None, copy=None, fastpath=<no_default>)

pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)

#Pandas numpy
#The input to series is LIST

#A pd.Series is a one-dimensional, labeled array in the pandas library, capable of holding any data type. 
#It is conceptually similar to a single column in a spreadsheet or a SQL table, where the labels are the row indices

s = pd.Series([1,2,3,4,5,6,7,8,np.nan,9])
print(s)

o/p:
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
5    6.0
6    7.0
7    8.0
8    NaN
9    9.0
dtype: float64

s = pd.Series(['Latesh','Ruchi','Vaneesa','Kishor','Sangita',np.nan])

o/p:
0     Latesh
1      Ruchi
2    Vaneesa
3     Kishor
4    Sangita
5        NaN

## Creating a Series from a dictionary with custom string labels
dict_data = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(dict_data)

o/p:
a    1
b    2
c    3
dtype: int64

s.str.upper() # Convert series in Upper case

s.str.lower() # Convert series in lower case

s.count() # count of series
o/p: 5

s.value_counts() # count of each values in the series.

Latesh     1
Ruchi      1
Vaneesa    1
Kishor     1
Sangita    1
dtype: int64

ser_index = [1,2,3,4,5,6,7,8,9,10,11,12]
s = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12], index = ser_index).shift(2)   # shift the first 2 values by 2 Position, last 2 values lost and first two values has NaN
print(s)

1      NaN
2      NaN
3      1.0
4      2.0
5      3.0
6      4.0
7      5.0
8      6.0
9      7.0
10     8.0
11     9.0
12    10.0
dtype: float64


d = pd.date_range('20250101',periods=12,freq='M')
print(d)

o/p:
DatetimeIndex(['2025-01-31', '2025-02-28', '2025-03-31', '2025-04-30',
               '2025-05-31', '2025-06-30', '2025-07-31', '2025-08-31',
               '2025-09-30', '2025-10-31', '2025-11-30', '2025-12-31'],
              dtype='datetime64[ns]', freq='M')

d = pd.date_range('20250101',periods=12,freq='D')
print(d)

o/p:
DatetimeIndex(['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04',
               '2025-01-05', '2025-01-06', '2025-01-07', '2025-01-08',
               '2025-01-09', '2025-01-10', '2025-01-11', '2025-01-12'],
              dtype='datetime64[ns]', freq='D')

# syntax : np.random.randint(low, high=None, size=None, dtype=int)              
data = np.random.randn(12,4) #(rows,columns)
index = pd.date_range('20250101',periods=12,freq='D')
columns = ['A','B','C','D']
df1 = pd.DataFrame(data=data, index=index,columns=columns)
print(df1)

o/p:
                   A         B         C         D
2025-01-01 -1.331857 -0.409665 -0.762912 -0.337357
2025-01-02 -0.259456 -0.930708 -0.499831  0.758003
2025-01-03 -0.671065  0.250940 -1.260347 -0.443040
2025-01-04 -2.213515 -0.476260 -2.201709 -0.033190
2025-01-05  1.425780 -0.708390  1.048761  0.944944
2025-01-06  0.605670  0.103434 -0.296056  1.094197
2025-01-07 -0.198285  0.484493 -0.897787  1.691761
2025-01-08 -0.021214 -0.562336 -0.857646 -0.051034
2025-01-09  0.297012  0.143870 -0.344272  0.744779
2025-01-10 -0.494997 -0.201508  0.598068  0.820388
2025-01-11 -0.048633 -0.372253  2.718450 -0.289866
2025-01-12 -0.828825 -2.280348 -1.450998  0.815397

#pandas with dict
df2 = pd.DataFrame({'A':[1,2,3,4],
                   'B':pd.Timestamp('20210101'),
                   'C':pd.Series(1,index=list(range(4)), dtype = 'float32'),
                   'D':np.array([5]*4, dtype = 'int32'),
                   'E':pd.Categorical(['true','False','True','false']),
                   'F': 'Eudereka'
                  })

df2

#Pandas using From a Python Dictionary
import pandas as pd
data = {
    'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
    'Age': [20, 21, 19, 18]
}
df = pd.DataFrame(data)
print(df)

#Pandas using a List of Dictionaries
import pandas as pd
data = [
    {'Name': 'Tom', 'Age': 20},
    {'Name': 'Nick', 'Age': 21},
    {'Name': 'Krish', 'Age': 19},
    {'Name': 'Jack', 'Age': 18}
]
df = pd.DataFrame(data)
print(df)

#Pandas using List of List
import pandas as pd
data = [
    ['Tom', 20],
    ['Nick', 21],
    ['Krish', 19],
    ['Jack', 18]
]
columns=['Name', 'Age']
df = pd.DataFrame(data=data,columns=columns )
print(df)

#Pandas using NumPy Array 
import pandas as pd
import numpy as np
data = np.array([
    ['Tom', 20],
    ['Nick', 21],
    ['Krish', 19],
    ['Jack', 18]
])
columns=['Name', 'Age']
df = pd.DataFrame(data=data,columns=columns )
print(df)

#Convert Spark Dataframe to Pandas
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
data = [ #LIST of LIST's
    ['Tom', 20],
    ['Nick', 21],
    ['Krish', 19],
    ['Jack', 18]
]

data = [ #LIST of SET's
    ('Tom', 20),
    ('Nick', 21),
    ('Krish', 19),
    ('Jack', 18)
]

columns=['Name', 'Age']
df = spark.createDataFrame(data,columns )
df = df.toPandas()
print(df)

#Convert Pandas Dataframe to Spark
from pyspark.sql import SparkSession
import pandas as pd
spark = SparkSession.builder.getOrCreate()
data = [
    ['Tom', 20],
    ['Nick', 21],
    ['Krish', 19],
    ['Jack', 18]
]
columns=['Name', 'Age']
df = pd.DataFrame(data=data,columns=columns )
df = spark.createDataFrame(df)
print(df)

CSV files: pd.read_csv('filename.csv')
Excel files: pd.read_excel('filename.xlsx')
SQL databases: pd.read_sql(query, connection)
JSON files: pd.read_json('filename.json')
Parquet file : pd.read_parquet(BytesIO(df_parquet_bytes))   # df_parquet_bytes = b'PAR1\x15\x04\x15P\x15<L\x15\n\x15\x00

--------------------------------------------------------------------

import pandas as pd
data = [ #list of list
    ['Tom', 20 , 'M',99.12],
    ['Nick', 21 ,'M',45.13],
    ['Krish', 19 ,'F',67.34],
    ['Jack', 18, 'N',56.45]
]
columns=['Name', 'Age','Gender','Percentage'] # if column name do not provide then default column name is 0...n
index = [0,1,2,3]  # for 4 records. Index can start from zero or one or any user defined number, default index start from 0
df1 = pd.DataFrame(data=data,index=index,columns=columns )
print(df1)

df1.dtypes # show all the datatypes

df1.convert_dtypes() #Convert the DataFrame to use best possible dtypes.

df1.empty  # provide True or False value for the Dataframe is Empty or Not.

df1.head() # return default top 5 rows
 
df1.tail() # return default botton 5 rows

df1.head(2) # return top 2 rows

df1.tail(3) # return bottom 3 rows

df1.index # return index start, stop and its range RangeIndex(start=0, stop=4, step=1)

df1.columns # Index(['Name', 'Age'], dtype='object')

df1.to_numpy #Convert the DataFrame to a NumPy array


<bound method DataFrame.to_numpy of     Name  Age Gender  Percentage
0    Tom   20      M       99.12
1   Nick   21      M       45.13
2  Krish   19      F       67.34
3   Jack   18      N       56.45>

df1.to_numpy() #Convert the DataFrame to a NumPy array but Output is LIST Of LIST , More Formatted

[['Tom' 20 'M' 99.12]
 ['Nick' 21 'M' 45.13]
 ['Krish' 19 'F' 67.34]
 ['Jack' 18 'N' 56.45]]
 
df1.describe()  #provide the mean,max,avg,count,std..etc number parameters.

df1.sort_index() # default sorting with index 0 and in asceneding order of index , Its just temporary in memory.

df2= df1.sort_index(ascending= False) # create the new dataframe with decending order of index. 

df1.sort_index(axis=0,ascending= False)   # axis = 0 | ‘index’ and 1 | ‘columns’ , default 0  , default sort is ascending , to do decending use ascending=False

df1.sort_values(by = 'Age')  # sort the dataframe via column age. Note: The display output will show the index order based on the sorted values.

df1['Age']  or df1[['Age']]  # Select the limited columns 

df1[["Name","Age"]]  # Select the limited columns but this time list of list

df1[0:3] # show rows from index 0 to index 3  # here selection or filteration of the columns not done, hence iloc is required.

df1[2:4] # show rows from index 2 to index 4


d1 = pd.DataFrame(data=np.random.randn(3,3))

          0         1         2
0 -0.118367 -0.228649 -1.038505
1  0.539759  0.122341 -1.013558
2 -0.105792  0.644055  2.737079


d1[:2]
          0         1         2
0 -1.624222  0.395909 -0.788680
1  1.486552  1.473814 -1.453094

d1[1:2]

          0         1         2
1  1.486552  1.473814 -1.453094

[d1[:2],d1[1:2]]

[          0         1         2
0 -1.624222  0.395909 -0.788680
1  1.486552  1.473814 -1.453094,           0         1         2
1  1.486552  1.473814 -1.453094]


df1.loc[rows,columns]  # High level syntax        Access a group of rows and columns by label(s) or a boolean array.

df1.loc[index[2]] # provide output of the index 2 but convert the row into column ( The Output is Series Format )  , Here columns are not provided.

df1.loc[index[1]] # provide output of the index 1 but convert the row into column ( The Output is Series Format ) , Here columns are not provided.

Name           Nick
Age              21
Gender            M
Percentage    45.13
Name: 1, dtype: object

df1.loc[:,['Name','Age','Gender']]  # show all rows but filtered columns.

    Name  Age Gender
0    Tom   20      M
1   Nick   21      M
2  Krish   19      F
3   Jack   18      N

df1.loc['2':'4',['Name','Age','Gender']] # show the rows from index 2 to 4 and filter limited columns.
df1.loc[2:4,['Name','Age','Gender']]  # both index with string and without string will work.

    Name  Age Gender
2  Krish   19      F
3   Jack   18      N

df1.loc[3,['Name','Age','Gender']] # show the index 3 records with limied column , the output is Series
Name      Jack
Age         18
Gender       N
Name: 3, dtype: object

df1.loc[index[3],['Name','Age','Gender']] # show the index 3 records with limied column , the output is Series
o/p:
Name      Jack
Age         18
Gender       N
Name: 3, dtype: object

df1.loc[3:3,['Name','Age','Gender']] # show the index 3 records with limied column , the output is table
   Name  Age Gender
3  Jack   18      N

df1.loc[:] # Shows all the rows and columns same as print(df1)

df1.at[index[0],'Age'] # shows the index[0] , column Age ,single value. Access a single value for a row/column label pair.

df1.at[index[3],'Gender']  # shows the index[3] , column Gender ,single value. Access a single value for a row/column label pair.

#iloc[row_integer_number,column_integer_number] Purely integer-location based indexing for selection by position. Deprecated since pandas version 2.2.0

df1.iloc[2] # Only Index 2 rows ,converted to series

Name          Krish
Age              19
Gender            F
Percentage    67.34
Name: 2, dtype: object

df1.iloc[1:3]   # from index 1 to 3 , all the columns

df1.iloc[1:3,1:3] # from index 1 to 3 , but column Age(1) and Gender (2)

   Age Gender
1   21      M
2   19      F

df1[df1['Age']>20] # ROW level Filters the dataframe for the WHERE Age > 20 , Only filter records will come in the output.

   Name  Age Gender  Percentage
1  Nick   21      M       45.13

df1['Age']>20 # Row level Filters the dataframe for the WHERE Age > 20 , but Boolean Values True , False will come in the o/p

0    False
1     True
2    False
3    False
Name: Age, dtype: bool

df1[   (df1['Age']>20) & (df1['Name']=='Nick') ]  # Applying multiple row level filters.
   Name  Age Gender  Percentage
1  Nick   21      M       45.13

df1.filter(items=['Name', 'Age']) # COLUMN level Filters the dataframe for the limited number of the columns
df1.filter(['Name', 'Age']) # COLUMN Filters the dataframe for the limited number of the columns
#df1[["Name","Age"]]

    Name  Age
0    Tom   20
1   Nick   21
2  Krish   19
3   Jack   18

df1[   (df1['Age']>20) & (df1['Name']=='Nick') ].filter(['Name', 'Age']) # both row and column level filters. 

& -> AND
| -> OR
~ -> NOT 

   Name  Age
1  Nick   21

df1.query("Age > 20 and Name == 'Nick' ") #SQL way to apply the row level filters

age=20
name='Nick'

df1.query("Age > @age and Name == @name ") #SQL way to apply the filters and replace the variable values.

new_index=[10,20,30,40]

# Apply the new index to existing dataframe but Data become NaN ( Null / None)
#Conform DataFrame to new index with optional filling logic.
#Places NA/NaN in locations having no value in the previous index. 
#A new object is produced unless the new index is equivalent to the current one and copy=False

df1.reindex(new_index)  # here new list of the index is provided, Hence NaN is coming. The new index values and old index values both are NOT matching.
   Name  Age Gender  Percentage
10  NaN  NaN    NaN         NaN
20  NaN  NaN    NaN         NaN
30  NaN  NaN    NaN         NaN
40  NaN  NaN    NaN         NaN

new_index=[1,2,3,4] # here new index=4 is added in the current dataframe , Hence for the new Index=4 , NaN is added. The Index 1,2,3 are common index, hence they are added.
df1.reindex(new_index)

    Name   Age Gender  Percentage
1   Nick  21.0      M       45.13
2  Krish  19.0      F       67.34
3   Jack  18.0      N       56.45
4    NaN   NaN    NaN         NaN

df1.reindex(index=new_index,fill_value=0) # replace the 0 with NaN values. i.e Optional Filling Logic.

    Name  Age Gender  Percentage
1   Nick   21      M       45.13
2  Krish   19      F       67.34
3   Jack   18      N       56.45
4      0    0      0        0.00

df1.reindex(index=new_index,columns = list(df1.columns))  # Return all the columns

    Name   Age Gender  Percentage
1   Nick  21.0      M       45.13
2  Krish  19.0      F       67.34
3   Jack  18.0      N       56.45
4    NaN   NaN    NaN         NaN

df1.reindex(index=new_index,columns = ['Name','Age']) #Return Limited columns

    Name   Age
1   Nick  21.0
2  Krish  19.0
3   Jack  18.0
4    NaN   NaN


df2 = df1.reindex(index=new_index,columns = list(df1.columns))
df2.isnull() # NaN = null = TRUE   :    Not NaN = FALSE        isnull is an alias for isna.

    Name    Age  Gender  Percentage
1  False  False   False       False
2  False  False   False       False
3  False  False   False       False
4   True   True    True        True

df2.isnull().count() # Count of the Not NaN values for each columns.   True and False both are Not NaN values.

Name          4
Age           4
Gender        4
Percentage    4
dtype: int64

df2.count() # Count of the Not NaN values for each columns.

Name          3
Age           3
Gender        3
Percentage    3
dtype: int64

columns_to_drop = ['column_name_1', 'column_name_2']
df2 = df2.drop(columns=columns_to_drop)

df2 = df2.drop("Percentage",axis=1)
#axis=1: Specifies that you are dropping a column (or 'columns' can be used as an alternative name)

df2.dropna() # Drop all the rows where values is NaN or any column with value is NaN . Drop the rows where at least one element is missing.

    Name   Age Gender  Percentage
1   Nick  21.0      M       45.13
2  Krish  19.0      F       67.34
3   Jack  18.0      N       56.45

df2.dropna(axis='columns') #Drop the single or all columns where at least one element is NaN.
# as all the column has single NaN values.
Empty DataFrame
Columns: []
Index: [1, 2, 3, 4] 

df2.fillna(value = 3) # Replaced NaN with value 3

    Name   Age Gender  Percentage
1   Nick  21.0      M       45.13
2  Krish  19.0      F       67.34
3   Jack  18.0      N       56.45
4      3   3.0      3        3.00

df2.isna() #isnull is an alias for isna

    Name    Age  Gender  Percentage
1  False  False   False       False
2  False  False   False       False
3  False  False   False       False
4   True   True    True        True

# Addition of the new column in the pandas dataframe
df = pd.DataFrame({"animal": ["dog", "pig"], "age": [10, 20]})
new_df = pd.eval("double_age = df.age * 2", target=df)


# Addition of the new column in the pandas dataframe
# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6 ]})
# Create the data for the new column (as a list, Series, or array)
new_column_data = [7, 8, 9 ]
# Add the new column 'C'
df['C'] = new_column_data

ser = pd.Series([5, 6, np.nan]) # series single index and single column
ser.isna() #isnull is an alias for isna
0    False
1    False
2     True
dtype: bool

df1.mean()  #provide the mean i.e average value of the number columns

Age           19.50
Percentage    67.01

df1.mean(1) # provide the mean at axis = 1 level.

0    59.560
1    33.065
2    43.170
3    37.225


number_df = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])

number_df.sub(1) #Get Subtraction of dataframe and other, element-wise (binary operator sub).

           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359
 
number_df.add(1) #Get Addition of dataframe and other, element-wise (binary operator sub).

           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

number_df.mul(10) #Get Multiplication of dataframe and other, element-wise (binary operator sub).

           angles  degrees
circle          0     3600
triangle       30     1800
rectangle      40     3600

number_df.div(0.5) #Get Multiplication of dataframe and other, element-wise (binary operator sub).

           angles  degrees
circle        0.0    720.0
triangle      6.0    360.0
rectangle     8.0    720.0


#Make a copy of this object’s indices and data.
number_df_shallow = number_df.copy()
deep_df_shallow = number_df.copy(deep=False) #default = True
#When deep=True (default), a new object will be created with a copy of the calling object’s data and indices. 
#Modifications to the data or indices of the copy will not be reflected in the original object (see notes below).

#When deep=False, a new object will be created without copying the calling object’s data or index (only references to the data and index are copied). 
#Any changes to the data of the original will be reflected in the shallow copy (and vice versa).



#Apply a function along an axis of the DataFrame.
number_df.apply(np.cumsum) # Apply a Cumulutive Sum function on the top of the DataFrame.

           angles  degrees
circle          0      360
triangle        3      540
rectangle       7      900


number_df.apply(np.sqrt) # Apply a square root function on the top of the DataFrame.

             angles    degrees
circle     0.000000  18.973666
triangle   1.732051  13.416408
rectangle  2.000000  18.973666

number_df.apply(np.sum, axis=1) # Apply SUM on all the colummns of the dataframe for each row.

circle       360
triangle     183
rectangle    364
dtype: int64

# apply function on single column
def add_five(x):
    return x + 5
    
number_df['circle'] = number_df['circle'].apply(add_five)
number_df['circle_new'] = number_df['circle'].apply(add_five)

           angles  degrees
circle          5      360
triangle        8      180
rectangle       9      360

# apply function on many columns
def row_sum(row):
    return row['angles'] + row['degrees']

number_df['sum_of_cols'] = number_df.apply(row_sum, axis=1)

           angles  degrees  sum_of_cols
circle          5      360      365
triangle        8      180      188
rectangle       9      360      369

#df.apply(lambda x: expression, axis=0) # Default, applied to columns
#df.apply(lambda row: expression, axis=1) # Applied to rows
#lamda function : this are the No Name Functions and it does not store the compile object in memory

# apply the lamda function for all the columns in the dataframe.
number_df.apply(lambda x: x.max()) #apply a lamda function (max/min..etc) on the top of the dataframe  / Output all the columns with max/min values.

number_df.transform(lambda x: x + 1) # trasform a lamda function (max/min..etc) on the top of the dataframe  / Output all the columns with max/min values.

#The main difference is that transform() strictly requires the output to be the same shape as the input, ensuring a one-to-one mapping of rows, 
# while apply() is more flexible and can return results of different sizes, including a single aggregated value per group. 

Name            Tom
Age              21
Gender            N
Percentage    99.12
dtype: object

number_df.apply(lambda x: x.max() - x.min())  

angles       4
degrees    180
dtype: int64

# apply the lamda function for the single column in the dataframe.
number_df['angles_new'] = number_df['angles'].apply(lambda x: x**2)

           angles  degrees  angles_new
circle          0      360           0
triangle        3      180           9
rectangle       4      360          16

left = pd.DataFrame({'id':[1,2,3],
                     'name':['Latesh','Vaneesa','Vivanna']})
right = pd.DataFrame({'id':[2,3,4],
                     'dept':['Studunt','Playing',np.nan]})

# all three are same , Note : Merge except all the input dataframe
pd.merge(left,right,on='id') 
pd.merge(left,right,left_on='id',right_on='id')
pd.merge(left,right,left_on='id',right_on='id',how='inner')

   id     name     dept
0   2  Vaneesa  Studunt
1   3  Vivanna  Playing

pd.merge(left,right,left_on='id',right_on='id',how='left') # how{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘inner’

-------------------------------
   id     name     dept
0   1   Latesh      NaN
1   2  Vaneesa  Studunt
2   3  Vivanna  Playing

pd.merge(left,right,left_on='id',right_on='id',how='left').filter(['id','name']) # join + filter of the columns

-------------------------------
   id     name
0   1   Latesh
1   2  Vaneesa
2   3  Vivanna

left.join(right,lsuffix='id',rsuffix='id',how='left').filter(['id','name']) #how{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘left’

#error : ValueError: cannot reindex on an axis with duplicate labels
# to do this join both left and right table has different join column name. The same id column name is not allowed.

df1 = pd.DataFrame({'name': ['john', 'mary', 'john'], 'age': [24, 45, 24]})
df2 = pd.DataFrame({'name': ['mary', 'john', 'susan'], 'age': [45, 89, 31]})

# Union all rows using concat and make new dataframe
df_union_all = pd.concat([df1, df2], ignore_index=True)

# return the unique value from the dataframe single column.
pd.unique(df_union_all["name"])

grp_by = pd.DataFrame({'id':[1,2,3],'name':['Latesh','Vaneesa','Vivanna'],'gender':['M','F','F']})
grp_by.groupby('gender').count()

        id  name
gender          
F        2     2
M        1     1

grp_by.groupby('gender').max()  # group by gender, shows all the columns

        id     name
gender             
F        3  Vivanna
M        1   Latesh

grp_by.groupby('gender').max('id') # group by gender, shows only id column

        id
gender    
F        3
M        1

grp_by.groupby([c1,c2,c3]).max('id') # group  by with multiple column's in the form of the list


my_list = list(zip([1,2,3,4,5,6,7,8],[6,7,8,9,10,11,12,13]))

[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (6, 11), (7, 12), (8, 13)]

index = pd.MultiIndex.from_tuples(my_list,names=['First','Second']) # note : here 2 Index keys are prepared.

pd.DataFrame(data = np.random.randn(8,2) , index = index , columns = ['A','B'])

                     A         B
First Second                    
1     6       0.158666  1.303793
2     7       0.517559  0.250480
3     8      -1.212285 -0.914899
4     9       0.783683  0.754437
5     10      0.751975 -0.256441
6     11     -1.261826  1.733873
7     12     -0.978752  1.393610
8     13     -0.452154 -0.164517


print(number_df)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

print(number_df.stack())   # convert columns into multiple rows.
circle     angles       0
           degrees    360
triangle   angles       3
           degrees    180
rectangle  angles       4
           degrees    360
dtype: int64


df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})


pivot_table_df = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']) # Create a spreadsheet-style pivot table as a DataFrame.
#The index levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.

C        large  small
A   B                
bar one    4.0    5.0
    two    7.0    6.0
foo one    2.0    1.0
    two    NaN    3.0
    
pivot_table_df = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc="sum") # apply the aggregrate function

C        large  small
A   B                
bar one    4.0    5.0
    two    7.0    6.0
foo one    4.0    1.0
    two    NaN    6.0

pivot_table_df = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc="sum", fill_value=0) # Fill the NaN with 0 value.    

C        large  small
A   B                
bar one      4      5
    two      7      6
foo one      4      1
    two      0      6
    
dates = pd.date_range('01/01/2021',periods = 100 , freq = 'S')
ts = pd.Series(np.random.randint(0,500,len(dates)),dates)
ts.resample('5min').sum()

o/p:
Freq: S, Length: 100, dtype: int32
2021-01-01    24998
Freq: 5T, dtype: int32



dates = pd.date_range('01/01/2021 00:00',periods = 100 , freq = 'S')
ts = pd.Series(data=np.random.randn(len(dates)),index=dates)
ts = ts.tz_localize('UTC') # convert the index dates in the UTC timezone
ts.tz_convert('US/Eastern') # convert the UTC timezone to US timezone

dates = pd.date_range('01/01/2021',periods = 5, freq = 'M')
ts = pd.Series(np.random.randn(len(dates)),dates)
ps = ts.to_period() # removed the dates from the index , the output index has just values 2021-01..2021-05
ps.to_timestamp() # conver the index value 2021-01..2021-05 to timestamp with dates in it. 2021-01-01 .. 2021-05-01

df7 = pd.DataFrame({'id':[1,2,3,4,5,6],
                    'name':['Latesh','Ruchi','Vaneesa','Sangita','Kishor','Sangani'],
                    'grade' : ['a','b','c','d','e','f']
                   })

before :
   id     name grade
0   1   Latesh     a
1   2    Ruchi     b
2   3  Vaneesa     c
3   4  Sangita     d
4   5   Kishor     e
5   6  Sangani     f

print(df7['grade'].astype("category"))
o/p:
0    a
1    b
2    c
3    d
4    e
5    f
Name: grade, dtype: category
Categories (6, object): ['a', 'b', 'c', 'd', 'e', 'f']

df7['grade'] = df7['grade'].astype("category") #Cast a pandas object to a specified dtype and later stored in same column.
df7["grade"].cat.categories = ["cat1","cat2","cat3","cat4","cat5","cat6"]  # assignment of the new category class.
df7['grade'] = df7["grade"].cat.set_categories(["cat1","cat2","cat3","cat4","cat5","cat6"]) # set the new categories

After :
   id     name grade
0   1   Latesh  cat1
1   2    Ruchi  cat2
2   3  Vaneesa  cat3
3   4  Sangita  cat4
4   5   Kishor  cat5
5   6  Sangani  cat6

#plt.close("all")

ts = pd.Series(data = [1,2,3,4,5] , index = pd.date_range('01/01/2021',periods = 5))

2021-01-01    1
2021-01-02    2
2021-01-03    3
2021-01-04    4
2021-01-05    5

ts = ts.cumsum() # cumulutive sum of the data

2021-01-01     1
2021-01-02     3
2021-01-03     6
2021-01-04    10
2021-01-05    15

ts.plot()  # Make plots of Series or DataFrame.
AxesSubplot(0.125,0.11;0.775x0.77)


to_csv(path_or_buf=None, *, sep=','...) # default delimiter is commo
ts.to_csv("ts.csv") # Write object to a comma-separated values (csv) file in current path

pd.read_csv(r"C:\Users\latesh.sangani\ts.csv")

#  read and write into DB using pandas

#!/usr/bin/env python
# coding: utf-8
# read and write using pandas.

sample raw file : my csv#.csv

EMP-ID,EMP NAME,EMP AGE,EMP ADD),EMP DOB?,EMP_AMT$M
1,Latesh Sangani,36,Hillock Tower,05-09-1985
2,Ruchi Sangani,35,Hillock Tower,29-11-1986
3,Kishor Sangani,66,Hillock Tower,15-07-1955
4,Sangita Sangani,60,Hillock Tower,16-12-1960
5,Vaneesa Sangani,06,Hillock Tower,29-11-2015
6,NULL,NULL,NULL,NULL


# import libraries
# conda install psycopg2
# pip install psycopg2

import os
import numpy as np
import pandas as pd
import psycopg2  #postgre data base libarary

ls *.csv
df = pd.read_csv("my csv#.csv")          # pyspark df = spark.read.csv("my csv#.csv",header=True,inferSchema=True)
df.head(10)
# clean table name
# lower case letters
# remove all white spaces
# replace -,/,\\,# with _

file = 'my csv#'
clean_table_name = file.lower().replace(" ","_").replace("?","").replace("$","").replace("-","_").replace(r"/","_").replace("\\","_").replace("%","") .replace(")","").replace(r"()","").replace("#","")
print(clean_table_name)
# clean header name
# lower case letters
# remove all white spaces
# replace -,/,\\,$ with _

df.columns
df.columns = [x.lower().replace(" ","_").replace("?","") .replace("$","_").replace("-","_").replace(r"/","_").replace("\\","_").replace("%","") .replace(")","").replace(r"(","").replace("#","") for x in df.columns]
df.columns
df.dtypes
print(f"create table {clean_table_name} ( emp_id int, emp_name varchar, emp_age float, emp_add varchar, emp_dob varchar, emp_amt_m float ) ")
replacements = {
    'object':'varchar',
    'float64':'float',
    'int64':'int'
}
print(replacements)

col_str = ", ".join("{} {}".format(n, d) for (n, d) in zip(df.columns,df.dtypes.replace(replacements)))
print(col_str)

#open a databae connection
conn_string = "host=database-yt.coxjb3ylifx.us-west-1.rds.amazonws.com  dbname='natdb'user='nate' password = 'test' "
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("connection open succussfully")

# drop table of the same new name want  to create
cursor.execute(f"drop table if exists {clean_table_name};")

#create table
cursor.execute(f"create table {clean_table_name} ( emp_id int, emp_name varchar, emp_age float, emp_add varchar, emp_dob varchar, emp_amt_m float ) ")

#insert values to table
#save df to csv
df.to_csv('my_csv.csv',header=df.columns,index = False,encoding = 'utf-8')

#open the new csv file prepared to save as object in the database
new_file = open('my_csv.csv')
print('file opened in memory')

for i in new_file:
    print(i)

#upload new my_csv.csv csv file into DB
SQL_STMT = """
COPY my_csv FROM STDIN WITH
     CSV 
     HEADER 
     DELIMITER AS ","
"""
cursor.copy_expert(sql=SQL_STMT,file=new_file)
print("file my_csv.csv copied in the table my_csv")

cursor.execute("grant select on table my_csv to public")
conn.commit()
conn.close()
print('table data loaded')




https://www.oracle.com/news/connect/run-sql-data-queries-with-pandas.html

------------------------------------sql----------------------
import pandas as pd
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
try:
   engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
   orders_sql = """SELECT * FROM orders"""; 
   df_orders = pd.read_sql(orders_sql, engine)
   details_sql = """SELECT * FROM details""";
   df_details = pd.read_sql(details_sql, engine)
   print(df_orders) 
   print(df_details) 
except SQLAlchemyError as e:
   print(e)
   
------------------------------------csv----------------------   
df = pd.read_csv("file_name.csv")
df.to_csv('my_csv.csv',header=df.columns,index = False,encoding = 'utf-8')   
------------------------------------excel----------------------   
# not working 
df = pd.read_excel(open('Pandas_Excel.xlsx', 'r'),
              sheet_name='Home')
print(df)   

# working
df1 = pd.DataFrame(data = [['latesh', '40'], ['Ruchi', '39']],index=['row 1', 'row 2'],columns=['name', 'age'])
df1.to_excel("output.xlsx")


------------------------------------parquet----------------------
# working 
# Convert dataframe to Parqut file and read parquet content in the pandas dataframe
from io import BytesIO
original_df = pd.DataFrame(
    {"foo": range(5), "bar": range(5, 10)}
   )
#print(original_df)
df_parquet_bytes = original_df.to_parquet()
print(df_parquet_bytes)
restored_df = pd.read_parquet(BytesIO(df_parquet_bytes))
#print(restored_df)

o/p: parquet content
b'PAR1\x15\x04\x15P\x15<L\x15\n\x15\x00\x12\x00\x00(\x00\x00\r\x01\x00\x01\r\x08...