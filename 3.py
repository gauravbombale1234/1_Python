# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:42:53 2023

@author: Omsai
Assignment
"""

import pandas as pd

df=pd.read_csv('C:/Gaurav/AutoInsurance.csv')

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
df2=df1.drop(['Gender','Income','Location Code','Marital Status'],axis=1)
print(df2)

#Assigning Row label
row_label2=['r1','r2','r3','r4']
df=pd.DataFrame(df2, index=row_label2)
print(df)

# Accesing particular row and coloumn
df3=df[2:2]
print(df3)


