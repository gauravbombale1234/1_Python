# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:18:46 2023

@author: Omsai
"""

import pandas as pd

df=pd.read_excel('C:/Gaurav/Coca_Rating_Ensemble.xlsx')
df

# data type of df
df.dtypes

# convert dtypes
df=df.convert_dtypes()
df.dtypes

# Apply as type
df=df.astype(str)

df = df.astype({"REF": float, "Cocoa_Percent": float})
print(df.dtypes)

##
cols=['Company','Name','REF','Review','Cocoa_Percent','Company_Location','Rating','Bean_Type','Origin']
df[cols]=df[cols].astype('string')
df.dtypes

##
df=df.astype({'REF':int},errors='ignore')
df.dtypes

## raise error
df=df.astype({'REF':int},errors='raise')
df.dtypes

#
df.size          
df.columns       
df.columns.values   
df.index         
df.dtypes 

#
df['Name']
df

#
df[['Name','Review']]
df

#
df2=df[6:]
df2

#
df['Name'][4]

#
df['Rating'-2]

##
df.describe()

#
df.rename(columns={'Company':'Company_Name','Rating':'Rate','Origin':'origin'},inplace=True)

#drop dataframe rows
df3=df.drop(df.index[1])
df3

# drop column
df3=df.drop(['Name'],axis=1)
df3

#
df3=df.drop(labels=['REF'],axis=1)
df3

##
df.drop(df.columns[1],axis=1)
df

#
df=pd.read_excel('C:/Gaurav/Coca_Rating_Ensemble.xlsx')
df
df.drop(df.columns[[1]],axis=1,inplace=True)
df

##
df2=df.iloc[:,0:2]
df2

''''''
#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df

df=pd.read_excel("C:/1-python/Coca_Rating_Ensemble.xlsx")
df

df2=df.iloc[:, 0:2]
df2

df2=df.iloc[0:2, :]
df2

#The second slice [:] indicates that all columns are required.

#Slicing Specific Rows and Columns using iloc attribute
df3=df.iloc[1:2, 1:3]
df3
#Another example
df3=df.iloc[:, 1:3]
df3
#The second operator [1:3] yields columns 1 and 3 only.
# Select Rows by Integer Index
df2 = df.iloc[2]
df2


df2 = df.iloc[[2,3,6]]  
df2
df2 = df.iloc[1:5] 
df2
df2 = df.iloc[:1]
df2    
df2 = df.iloc[:3]    

df2 = df.iloc[-3:]
   
df2 = df.iloc[::2]   

# Select Rows by Index Labels
df2 = df.loc[1]   
df2     
df2 = df.loc[[2,3,6]]  
df2  

df2 = df.loc[1:5]    
df2

df2 = df.loc[1:5]
df2 = df.loc[1:5:2]   
df2
##########################################

#Select Rows by Index using Pandas iloc[]
#Select Row by Integer Index

print(df.iloc[2])

# Select Rows by Index List
print(df.iloc[[2,3,6]])


# Select Rows by Integer Index Range
print(df.iloc[1:5])

# Select First Row by Index
print(df.iloc[:1])


# Select First 3 Rows
print(df.iloc[:3])


# Select Last Row by Index
print(df.iloc[-1:])


print(df.iloc[-3:])


df2=df['Company']
df2

## select multiple columns
df2 = df[["Company","Review","Cocoa_Percent"]] 
df2

# Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
## Selecte multiple columns

df2 = df.loc[:,["Company","Review","Cocoa_Percent"]]
df2

# Select Random columns 

df2 = df.loc[:, ["Company","Review","Cocoa_Percent"]]
df2

# Select columns between two columns 
df2 = df.loc[:,'Company':'Review'] 
df2

## Select columns by range
df2 = df.loc[:,'Review':] 
df2

# Select columns by range 

df2 = df.loc[:,:'Review']  

## Select every alternate column
df2 = df.loc[:,::2]
df2       
   

################################

#Pandas.DataFrame.query() by Examples

df2=df.query("Company == 'Zotter'")
print(df2)

############################

# not equals condition
df2=df.query("Company != 'Zotter'" and "Company != 'Zokoko'")
df2

##############################

#Pandas Add Column to DataFrame


#Pandas Add Column to DataFrame
# Add new column to the DataFrame
df2=df.drop(df.index[5:])
df2

Emp = ['Ram', 'sham', 'Ghansham', 'Ganesh', 'Ramesh']
df2 = df2.assign(Emp=Emp)
print(df2)
############################

# Add multiple columns to the DataFrame
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df2.assign(MNCComp = MNCCompanies,Emp=Emp )
df2

############################

#Append Column to Existing Pandas DataFrame
# Add New column to the existing DataFrame

df2["MNCCompanies"] = MNCCompanies
print(df)


#############################

# Add new column at the specific position

df2.insert(0,'Emp',Emp)
print(df)

######################

df.columns
print(df.columns)


print(df.columns)

#Quick Examples of Get the Number of Rows in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count

##################################

row_count = df.shape[0]  # Returns number of rows
col_count = df.shape[1]  # Returns number of columns
print(row_count)

##################################

#pandas Apply Function to a Column
# Below are quick examples
# Using Dataframe.apply() to apply function add column


# Using apply function single column
def add_4(x):
   return x+4
df["Rating"] = df["Rating"].apply(add_4)
df["Rating"]

# Apply to multiple columns
df[['Rating','REF']] = df[['Rating','REF']].apply(add_4)
df

##################################

# apply() function on selected list of multiple columns


df[['Rating','REF']] = df[['Rating','REF']].apply(add_4)
print(df)

##############################

#Apply Lambda Function to Single Column
# Using Dataframe.apply() and lambda function

df["Rating"] = df["Rating"].apply(lambda x: x-2)
print(df)

#Using pandas.DataFrame.transform() to Apply Function Column
# Using DataFrame.transform() 

def add_2(x):
    return x+2
df2 = df.transform(add_2)
print(df)

#Using pandas.DataFrame.map() to Single Column

df['Rating'] = df['Rating'].map(lambda A: A/2.)
print(df)

#Using Numpy function on single Column
# Using Dataframe.apply() & [] operator

import numpy as np
df['Rating'] = df['Rating'].apply(np.square)
print(df)

#########################
#Using NumPy.square() Method
# Using numpy.square() and [] operator
df['REF'] = np.square(df['REF'])
print(df)

# Use groupby() to compute the sum
df2 =df.groupby(['Rating']).sum()
print(df2)

# Group by multiple columns
df2 =df.groupby(['Rating', 'REF']).sum()
print(df2)

# Add Index to the grouped data
# Add Row Index to the group by result

df2 = df.groupby(['Rating', 'REF']).sum().reset_index()
print(df2)

# Group by on multiple columns
df2 =df.groupby(['Rating', 'REF']).sum()
print(df2)

##############################
#Pandas Get Column Names from DataFrame
import pandas as pd
import numpy as np


df.columns
# Get the list of all column names from headers

column_headers = list(df.columns.values)
print("The Column Header :", column_headers)

#Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers

#Using list(df) to get the list of all Column Names
column_headers = list(df)
column_headers

############################

#Pandas Shuffle DataFrame Rows 

#Pandas Shuffle DataFrame Rows

# shuffle the DataFrame rows & return all rows

df1 = df.sample(frac = 1)
print(df1)

# Create a new Index starting from zero
df1 = df.sample(frac = 1).reset_index()
print(df1)

# Drop shuffle Index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)

#pandas inner join is mostly used join, 
#It is used to join two DataFrames on indexes. 
#When indexes don’t match the rows get dropped from both DataFrames.
##################################################

# pandas join ,by default it will join the table left join
df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)

# pandas Inner join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)

 #pandas Left join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='left')
print(df3)
 #pandas Right join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)



################################

#Concatenate Multiple DataFrames Using pandas.concat()
  
# Appending multiple DataFrame
df3 = pd.concat([df, df1, df2])
print(df3)

# Using Series.values.tolist()
col_list = df.Courses.values.tolist()
print(col_list)

# Using Series.values.tolist()
col_list = df["Company"].values.tolist()
print(col_list)

# Using list() Function
col_list =  list(df["Company"])
print(col_list)

# Conver to numpy array
col_list = df['Company'].to_numpy()
print(col_list)

# Get by Column Index
col_list = df[df.columns[0]].values.tolist()
print(col_list)

# Convert Index Column to List
index_list = df.inde



"""
Practice
"""
# -- coding: utf-8 --
"""
Created on Sun May 28 13:15:08 2023

@author: Gaurav

"""

import pandas as pd

df=pd.read_csv("C:/1-python/Company_Data.csv")
df

df.dtypes

# Convert dtypes 
df=df.convert_dtypes()
df.dtypes

# Apply as type
df=df.astype(str)

df = df.astype({"CompPrice": float, "Price": float})
print(df.dtypes)

df = df.astype(str)
df.dtypes

cols=['Sales','CompPrice','Price','ShelveLoc']
df[cols] = df[cols].astype('string')
df.dtypes

#Ignores error
df = df.astype({"Age": int},errors='ignore')
df.dtypes

# Generates error
df = df.astype({"Age": int},errors='raise')

#DataFrame properties
df.shape

df.size

df.columns

df.columns.values

df.index

#Accessing one column contents
df['Age']

##Accessing two columns contents
df[['Price','Age']]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2

# Accessing certain cell from column
df['Age'][4]

# Substracting specific value from column
df['Sales']=df['Sales'] -1 

# Describe DataFrame for all numberic columns
df.describe()


#  Rename column 

df2 = df.rename({'Sales': 'company', 'Age': 'Rate'}, axis='columns')
df2
df2 = df.rename(columns={'Sales': 'company', 'Age': 'Rate'})

df=df.rename(columns={'Sales': 'company', 'Age': 'Rate'},inplace=True)
df

# Drop DataFrame rows
df1=df.drop(df.index[1])

df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

# Delete Rows by Index Range
df1=df.drop(df.index[23:])
df1

# Drop column by names
df1=df.drop(['CompPrice'],axis=1)
df1

# Labels
df1=df.drop(labels=['Sales'],axis=1)
df1

# columns
df1=df.drop(columns=['Sales'],axis=1)
df1

# Drop Column by index
df.drop(df.columns[1],axis=1)
df

# Drop from Df 
# inplace used for main ope on df
df.drop(df.columns[[2]],axis=1,inplace=True)
df

# Drop two or more columns

lisCol = ["Sales","Age"]
df2=df.drop(lisCol, axis = 1)
print(df2)

# Drop two or columns by index

df2=df.drop(df.columns[[0,1]],axis=1)

# Drop multiple column
lisCol = ["Sales","Age"]
df2=df.drop(lisCol, axis = 1)
print(df2)

#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df

df=pd.read_csv("C:/1-python/Company_Data.csv")
df

df2=df.iloc[:, 0:2]
df2

df2=df.iloc[0:2, :]
df2

#The second slice [:] indicates that all columns are required.

#Slicing Specific Rows and Columns using iloc attribute
df3=df.iloc[1:2, 1:3]
df3
#Another example
df3=df.iloc[:, 1:3]
df3
#The second operator [1:3] yields columns 1 and 3 only.
# Select Rows by Integer Index
df2 = df.iloc[2]
df2


df2 = df.iloc[[2,3,6]]  
df2
df2 = df.iloc[1:5] 
df2
df2 = df.iloc[:1]
df2    
df2 = df.iloc[:3]    

df2 = df.iloc[-3:]
   
df2 = df.iloc[::2]   

# Select Rows by Index Labels
df2 = df.loc[1]   
df2     
df2 = df.loc[[2,3,6]]  
df2  

df2 = df.loc[1:5]    
df2

df2 = df.loc[1:5]
df2 = df.loc[1:5:2]   
df2
##########################################

#Select Rows by Index using Pandas iloc[]
#Select Row by Integer Index

print(df.iloc[2])

# Select Rows by Index List
print(df.iloc[[2,3,6]])


# Select Rows by Integer Index Range
print(df.iloc[1:5])

# Select First Row by Index
print(df.iloc[:1])


# Select First 3 Rows
print(df.iloc[:3])


# Select Last Row by Index
print(df.iloc[-1:])


print(df.iloc[-3:])


df2=df['Sales']
df2

## select multiple columns
df2 = df[["Sales","Age","CompPrice"]] 
df2

# Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
## Selecte multiple columns

df2 = df.loc[:,["Sales","Age","CompPrice"]]
df2

# Select Random columns 

df2 = df.loc[:, ["Sales","Age","CompPrice"]]
df2

# Select columns between two columns 
df2 = df.loc[:,'Sales':'Age'] 
df2

## Select columns by range
df2 = df.loc[:,'Sales':] 
df2

# Select columns by range 

df2 = df.loc[:,:'Age']  

## Select every alternate column
df2 = df.loc[:,::2]
df2       
   

################################

#Pandas.DataFrame.query() by Examples

df2=df.query("US == 'No'")
print(df2)

############################

# not equals condition
df2=df.query("US != 'No'" and "US != 'Yes'")
df2

##############################

#Pandas Add Column to DataFrame


#Pandas Add Column to DataFrame
# Add new column to the DataFrame
df2=df.drop(df.index[5:])
df2

Emp = ['Ram', 'sham', 'Ghansham', 'Ganesh', 'Ramesh']
df2 = df2.assign(Emp=Emp)
print(df2)
############################

# Add multiple columns to the DataFrame
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df2.assign(MNCComp = MNCCompanies,Emp=Emp )
df2

############################

#Append Column to Existing Pandas DataFrame
# Add New column to the existing DataFrame

df2["MNCCompanies"] = MNCCompanies
print(df)


#############################

# Add new column at the specific position

df2.insert(0,'Emp',Emp)
print(df)

######################

df.columns
print(df.columns)


print(df.columns)

#Quick Examples of Get the Number of Rows in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count

##################################

row_count = df.shape[0]  # Returns number of rows
col_count = df.shape[1]  # Returns number of columns
print(row_count)

##################################

#pandas Apply Function to a Column
# Below are quick examples
# Using Dataframe.apply() to apply function add column


# Using apply function single column
def add_4(x):
   return x+4
df["Age"] = df["Age"].apply(add_4)
df["Age"]

# Apply to multiple columns
df[['Age','Sales']] = df[['Age','Sales']].apply(add_4)
df

##################################

# apply() function on selected list of multiple columns


df[['Age','Sales']] = df[['Age','Sales']].apply(add_4)
print(df)

##############################

#Apply Lambda Function to Single Column
# Using Dataframe.apply() and lambda function

df["Age"] = df["Age"].apply(lambda x: x-2)
print(df)

#Using pandas.DataFrame.transform() to Apply Function Column
# Using DataFrame.transform() 

def add_2(x):
    return x+2
df2 = df.transform(add_2)
print(df)


#Using Numpy function on single Column
# Using Dataframe.apply() & [] operator

import numpy as np
df['Sales'] = df['Sales'].apply(np.square)
print(df)

#########################
#Using NumPy.square() Method
# Using numpy.square() and [] operator
df['Sales'] = np.square(df['Sales'])
print(df)

# Use groupby() to compute the sum
df2 =df.groupby(['Sales']).sum()
print(df2)



# Add Index to the grouped data
# Add Row Index to the group by result

df2 = df.groupby(['Age', 'Sales']).sum().reset_index()
print(df2)


##############################
#Pandas Get Column Names from DataFrame
import pandas as pd
import numpy as np


df.columns
# Get the list of all column names from headers

column_headers = list(df.columns.values)
print("The Column Header :", column_headers)

#Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers

#Using list(df) to get the list of all Column Names
column_headers = list(df)
column_headers

############################

#Pandas Shuffle DataFrame Rows 

#Pandas Shuffle DataFrame Rows

# shuffle the DataFrame rows & return all rows

df1 = df.sample(frac = 1)
print(df1)

# Create a new Index starting from zero
df1 = df.sample(frac = 1).reset_index()
print(df1)

# Drop shuffle Index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)

#pandas inner join is mostly used join, 
#It is used to join two DataFrames on indexes. 
#When indexes don’t match the rows get dropped from both DataFrames.
##################################################

# pandas join ,by default it will join the table left join
df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)

# pandas Inner join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)

 #pandas Left join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='left')
print(df3)
 #pandas Right join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)



################################


# Using Series.values.tolist()
col_list = df.Age.values.tolist()
print(col_list)

# Using Series.values.tolist()
col_list = df["Sales"].values.tolist()
print(col_list)

# Using list() Function
col_list =  list(df["Sales"])
print(col_list)

# Conver to numpy array
col_list = df['Sales'].to_numpy()
print(col_list)

# Get by Column Index
col_list = df[df.columns[0]].values.tolist()
print(col_list)



"""
Practice
"""
# -- coding: utf-8 --
"""
Created on Mon May 29 14:13:03 2023

@author: Gaurav

"""

import pandas as pd

df=pd.read_csv("C:/1-python/emp_data.csv")
df

df.dtypes

# Convert dtypes 
df=df.convert_dtypes()
df.dtypes

# Apply as type
df=df.astype(str)

df = df.astype({"CompPrice": float, "Price": float})
print(df.dtypes)

df = df.astype(str)
df.dtypes

cols=['Sales','CompPrice','Price','ShelveLoc']
df[cols] = df[cols].astype('string')
df.dtypes

#Ignores error
df = df.astype({"Age": int},errors='ignore')
df.dtypes

# Generates error
df = df.astype({"Age": int},errors='raise')

#DataFrame properties
df.shape

df.size

df.columns

df.columns.values

df.index

#Accessing one column contents
df['Age']

##Accessing two columns contents
df[['Price','Age']]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2

# Accessing certain cell from column
df['Age'][4]

# Substracting specific value from column
df['Sales']=df['Sales'] -1 

# Describe DataFrame for all numberic columns
df.describe()


#  Rename column 

df2 = df.rename({'Sales': 'company', 'Age': 'Rate'}, axis='columns')
df2
df2 = df.rename(columns={'Sales': 'company', 'Age': 'Rate'})

df=df.rename(columns={'Sales': 'company', 'Age': 'Rate'},inplace=True)
df

# Drop DataFrame rows
df1=df.drop(df.index[1])

df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

# Delete Rows by Index Range
df1=df.drop(df.index[23:])
df1

# Drop column by names
df1=df.drop(['CompPrice'],axis=1)
df1

# Labels
df1=df.drop(labels=['Sales'],axis=1)
df1

# columns
df1=df.drop(columns=['Sales'],axis=1)
df1

# Drop Column by index
df.drop(df.columns[1],axis=1)
df

# Drop from Df 
# inplace used for main ope on df
df.drop(df.columns[[2]],axis=1,inplace=True)
df

# Drop two or more columns

lisCol = ["Sales","Age"]
df2=df.drop(lisCol, axis = 1)
print(df2)

# Drop two or columns by index

df2=df.drop(df.columns[[0,1]],axis=1)

# Drop multiple column
lisCol = ["Sales","Age"]
df2=df.drop(lisCol, axis = 1)
print(df2)

#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df

df=pd.read_csv("C:/1-python/Company_Data.csv")
df

df2=df.iloc[:, 0:2]
df2

df2=df.iloc[0:2, :]
df2

#The second slice [:] indicates that all columns are required.

#Slicing Specific Rows and Columns using iloc attribute
df3=df.iloc[1:2, 1:3]
df3
#Another example
df3=df.iloc[:, 1:3]
df3
#The second operator [1:3] yields columns 1 and 3 only.
# Select Rows by Integer Index
df2 = df.iloc[2]
df2


df2 = df.iloc[[2,3,6]]  
df2
df2 = df.iloc[1:5] 
df2
df2 = df.iloc[:1]
df2    
df2 = df.iloc[:3]    

df2 = df.iloc[-3:]
   
df2 = df.iloc[::2]   

# Select Rows by Index Labels
df2 = df.loc[1]   
df2     
df2 = df.loc[[2,3,6]]  
df2  

df2 = df.loc[1:5]    
df2

df2 = df.loc[1:5]
df2 = df.loc[1:5:2]   
df2
##########################################

#Select Rows by Index using Pandas iloc[]
#Select Row by Integer Index

print(df.iloc[2])

# Select Rows by Index List
print(df.iloc[[2,3,6]])


# Select Rows by Integer Index Range
print(df.iloc[1:5])

# Select First Row by Index
print(df.iloc[:1])


# Select First 3 Rows
print(df.iloc[:3])


# Select Last Row by Index
print(df.iloc[-1:])


print(df.iloc[-3:])


df2=df['Sales']
df2

## select multiple columns
df2 = df[["Sales","Age","CompPrice"]] 
df2

# Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
## Selecte multiple columns

df2 = df.loc[:,["Sales","Age","CompPrice"]]
df2

# Select Random columns 

df2 = df.loc[:, ["Sales","Age","CompPrice"]]
df2

# Select columns between two columns 
df2 = df.loc[:,'Sales':'Age'] 
df2

## Select columns by range
df2 = df.loc[:,'Sales':] 
df2

# Select columns by range 

df2 = df.loc[:,:'Age']  

## Select every alternate column
df2 = df.loc[:,::2]
df2       
   

################################

#Pandas.DataFrame.query() by Examples

df2=df.query("US == 'No'")
print(df2)

############################

# not equals condition
df2=df.query("US != 'No'" and "US != 'Yes'")
df2

##############################

#Pandas Add Column to DataFrame


#Pandas Add Column to DataFrame
# Add new column to the DataFrame
df2=df.drop(df.index[5:])
df2

Emp = ['Ram', 'sham', 'Ghansham', 'Ganesh', 'Ramesh']
df2 = df2.assign(Emp=Emp)
print(df2)
############################

# Add multiple columns to the DataFrame
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df2.assign(MNCComp = MNCCompanies,Emp=Emp )
df2

############################

#Append Column to Existing Pandas DataFrame
# Add New column to the existing DataFrame

df2["MNCCompanies"] = MNCCompanies
print(df)


#############################

# Add new column at the specific position

df2.insert(0,'Emp',Emp)
print(df)

######################

df.columns
print(df.columns)


print(df.columns)

#Quick Examples of Get the Number of Rows in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])










