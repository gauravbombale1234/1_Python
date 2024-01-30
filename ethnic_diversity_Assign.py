# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:19:18 2023

@author: Omsai
"""

import pandas as pd

df=pd.read_csv('C:/Gaurav/ethnic diversity.csv')
df

#shape
df.shape
#size
df.size
#column
df.columns 
#column values      
df.columns.values 
#index  
df.index 
#Data Types        
df.dtypes 


# 7 values that describe DataFrame
df.describe()

#Delete Rows by index range
df1=df.drop(df.index[5:]) #delete other than first 5 rows
df1

# Drop at particular index
df1=df1.drop(0)
df1

# Delete columns
df2=df1.drop(['Position','State'],axis=1)
print(df2)

print(df)
print(df.dtypes)
#convert all types to best possible types
df3=df.convert_dtypes()
print(df3.dtypes)

#change all columns to same type
df3=df.astype(str)
print(df3.dtypes)

##ignore error
df2=df.astype({'State':int},errors='ignore')
df2.dtypes
##Generates error
df2=df.astype({'State':int},errors='raise')
df2.dtypes

#Delete Rows by Position/index
df1=df.drop(df.index[[1,4]])
df1

#Delete Rows by index range
df1=df.drop(df.index[2:])
df1

#
df1=df.drop([0,3])  #it will delete row0 and row3
df1

df1=df.drop(range(0,2)) #it will delete 0 and 1
df1

# Delete columns
#Explicitly using parameter name labels
df1=df.drop(labels=['Sex'],axis=1)
df1
#alternatively you can also use column instead of labels
df2=df.drop(columns=['age'],axis=1)
df2

#Drop column by index
print(df.drop(df.columns[1],axis=1))

#using replace=True  (means drop original DataFrame)
df
df.drop(df.columns[[2]],axis=1, inplace=True)
print(df)

#Drop two or more Columns by label name
df2=df.drop([' Number of times pregnant',' Class variable'],axis=1)
print(df2)

#Drop two or more columns by index
df2=df.drop(df.columns[[0,1]],axis=1)
df2


#############################
df2=df.iloc[:,0:2]
df2
#this line uses slicing operator to get DataFrame
#the first slice indicates to return all rows
#the second slice indicates to return all columns

df2=df.iloc[0:4,:]
df2

#
df3=df.iloc[1:2,1:3]
df3
#
df2=df.iloc[2]
df2
#
df2=df.iloc[[2,3,6]]  #select rows by index list
df2

###### select column using name or index
df2=df['age']
df2

############## Adding Columns
tutors=['Gaurav']
df2=df3.assign(TutorAssigned=tutors)
df2

#Rename column name
df2=df.rename(columns={'age':'Age'})
print(df2)
#Alternatively you can also write above code by using axis
df2=df.rename({'State':'state','Race':'race'},axis=1)
print(df2)
#
df2=df.rename({'State':'state'},axis='columns')
print(df2)
#In order to change existing dataframe without copying to existing dataframe
df.rename({'age':'AGE'},axis='columns',inplace=True)
print(df)
