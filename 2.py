# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:20:17 2023

@author: Omsai
"""
#Lambda Function (ananymous function)
# Name of function = lambda arguments : business logic
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))

add=lambda a,b,c:a+b+c
add(4,5,6)

##################
def multi(a,b,c):
    m=a*b*c
    return m
print(multi(4,5,6))

multi=lambda a,b,c:a*b*c
multi(4,5,6)

######################
val=lambda *args:sum(args)
val(1,2,3,4,5)

#########
def myfun(*args):
    for i in args:
        print(i)

myfun('hello','gaurav','welcome')

#same as above
fun=lambda *args:args
fun('Gaurav','Vaibhav','Rohit')

##################
def person(name , *data):
    print(name)
    print(data)
    
person('gaurav',21,'shrirampur',23433)

##################
def person(name, **data):
    print(name)
    print(data)
person(name='gaurav',data=12,hi='hii')

##############
def per(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
        
per(name='Gaurav',age=22,loc='shrirampur')

#############
val2=lambda **data:sum(data.values())
val2(a=2,b=33,c=2,d=3)

#
max=lambda a,b:a if(a>b) else b
print(max(17,2))

#################
per2=lambda **data:[print(i,j) for i,j in data.items() ]
per2(name='Gaurav',age=22,loc='shrirampur')

#
per2=lambda **data:[(j) for i,j in data.items() ]
per2(name='Gaurav',age=22,loc='shrirampur')

###############
lst1=[3,4,5,6,7]
sqr=lambda lst1:[i**2 for i in lst1]
print(sqr(lst1))

###############################
#Python for Data Science       
###############################
"""
Created on Tue May  2 09:19:32 2023

@author: Omsai
"""

import pandas as pd
pd.__version__      #for checking version

################data frame using list
import pandas as pd
technologies=[['spark',200000,'30days'],
              ['pandas',200000,'40days']
             ]
df=pd.DataFrame(technologies)
print(df)

############
coloumn_names=['Courses','Fee','Duration']
row_label=['a','b']
df=pd.DataFrame(technologies,columns=coloumn_names,index=row_label)
print(df)

########## data type of df
df.dtypes

###############
types={'Courses':str,'Fee':float,'Duration':str}
df.dtypes

###################dataframe using Dictionary
techn={
       'Courses':['saprk','PySpark','Hadoop'],
       'Fee':[200000,100000,300000],
       'Duration':['30days','60days','100days'],
       'Discount':[1000,2000,3000]
       }
df=pd.DataFrame(techn)
print(df)

########### converting dataframe to csv
df.to_csv('Data_file.csv')
#create DataFrame using CSV file
d=pd.read_csv('Data_file.csv')

"""
Created on Tue May  2 16:49:32 2023

@author: Omsai
"""
import pandas as pd
import numpy as np

techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       'Discount':[1000,2000,3000,0,500,2000,1000,2000]
       }
row_label2=['r1','r2','r3','r4','r5','r6','r7','r8']
df=pd.DataFrame(techn2, index=row_label2)
print(df)

#Properties
df.shape         # (8, 4)
df.size          #32
df.columns       #Index(['Courses', 'Fee', 'Duration', 'Discount'], dtype='object')
df.columns.values   #array(['Courses', 'Fee', 'Duration', 'Discount'], dtype=object)
df.index         #Index(['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8'], dtype='object')
df.dtypes        #

df['Courses']
df[['Courses','Fee']]
# Accesing particular row and coloumn
df2=df[6:]
print(df2)

#
df3=df[2:3]
print(df3)

df['Duration'][3]

#subtract particular value
df['Fee']=df['Fee']-200
print(df)

#gives 7 values that describe DataFrame
df.describe()

# Renames
df.columns=['A','B','C','D']
print(df)

###############
df=pd.DataFrame(techn2, index=row_label2)
df.columns=['A','B','C','D']
df2=df.rename({'A':'a1','B':'b1'}, axis=1)
df2=df.rename({'C':'c1','D':'d1'}, axis='columns')

df2=df.rename(columns={'A':'c1','B':'c2'})

"""
Created on Wed May  3 08:23:49 2023

@author: Omsai
"""
import pandas as pd
import numpy as np
techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       'Discount':[1000,2000,3000,0,500,2000,1000,2000]
       }
row_label2=['r1','r2','r3','r4','r5','r6','r7','r8']
df2=pd.DataFrame(techn2, index=row_label2)

print(df2)
print(df2.dtypes)
#convert all types to best possible types
df3=df2.convert_dtypes()
print(df3.dtypes)

#change all columns to same type
df2=df2.astype(str)
print(df2.dtypes)

#change type for one or Multiple column
df2=df2.astype({"Discount":float})
print(df2.dtypes)

#convert dataframe to its original datatype
df2=pd.DataFrame(techn2, index=row_label2)
#convert data type for all column in a list
cols=['Fee','Discount']
df2[cols]=df2[cols].astype('float')
df2.dtypes
#
cols=['Courses','Duration']
df2[cols]=df2[cols].astype('string')
df2.dtypes

"""
Created on Wed May  3 16:46:58 2023

@author: Omsai
"""
#Above code is necessary
##ignore error
df2=df2.astype({'Courses':int},errors='ignore')
df2.dtypes
##Generates error
df2=df2.astype({'Courses':int},errors='raise')
df2.dtypes

#converts feed column to numeric type
df2=df2.astype(str)
print(df2.dtypes)
df2['Discount']=pd.to_numeric(df2['Discount'])
df2.dtypes

#Drop rows by labels
print(df2)
df3=df2.drop(['r1','r2'])
print(df3)

#Delete Rows by Position/index
df1=df2.drop(df2.index[[1,4]])
df1

#Delete Rows by index range
df1=df2.drop(df2.index[2:])
df1

###############################
#When you have dafault indexs for rows
techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       'Discount':[1000,2000,3000,0,500,2000,1000,2000]
       }
df=pd.DataFrame(techn2)
df

df1=df.drop(0)
df1

#
df=pd.DataFrame(techn2)
df

df1=df.drop([0,3])  #it will delete row0 and row3
df1

df1=df.drop(range(0,2)) #it will delete 0 and 1
df1

######################
# Delete columns
techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       }
df=pd.DataFrame(techn2)
print(df)

df2=df.drop(['Fee'],axis=1)
print(df2)

"""
Created on Thu May  4 08:14:06 2023

@author: Omsai
"""
import pandas as pd
import numpy as np

techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       }
df=pd.DataFrame(techn2)
print(df)
# Delete columns
#Explicitly using parameter name labels
df1=df.drop(labels=['Fee'],axis=1)
df1
#alternatively you can also use column instead of labels
df2=df.drop(columns=['Fee'],axis=1)
df2

#Drop column by index
print(df.drop(df.columns[1],axis=1))

#using replace=True  (means drop original DataFrame)
df=pd.DataFrame(techn2)
df
df.drop(df.columns[[2]],axis=1, inplace=True)
print(df)
############
#Drop two or more Columns by label name
df=pd.DataFrame(techn2)
df
df2=df.drop(['Courses','Fee'],axis=1)
print(df2)

#Drop two or more columns by index
df=pd.DataFrame(techn2)
df
df2=df.drop(df.columns[[0,1]],axis=1)
df2

#############
#Drop columns from list of columns
df=pd.DataFrame(techn2)
df
liscol=['Courses','Fee']
df2=df.drop(liscol,axis=1)
print(df2)

#Remove columns from dataframe inplace
df.drop(df.columns[1],axis=1,inplace=True)
df

###########################
###########################
import pandas as pd
import numpy as np

techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       'Discount':[1000,2000,3000,0,500,2000,1000,2000]
       }
row_label2=['r1','r2','r3','r4','r5','r6','r7','r8']
df=pd.DataFrame(techn2, index=row_label2)
df
#IMPORTANT
#ILOC and LOC
"""
ILOC : Aceesing using index
  iloc[start_row:end_row , start_columns:end_columns]
LOC : Aceesing using label
"""
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

#
df2=df.iloc[1:5]
df2
#
df2=df.iloc[:1]
df2
#
df2=df.iloc[:3]
df2
#
df2=df.iloc[-1:]    #negative index
df2
#
df2=df.iloc[-3:]    #last 3 rows
df2
#
df2=df.iloc[:-3]    
df2
#
df2=df.iloc[::2]    #select alternate rows
df2

#select rows by index labels
df2=df.loc['r2']    #select r2 by index label
df2
#
df2=df.loc[['r2','r3','r6']]     #select r2,r3,r6 by index label
df2
#
"""
Created on Thu May  4 16:44:45 2023

@author: Omsai
"""
import pandas as pd
import numpy as np

techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       'Discount':[1000,2000,3000,0,500,2000,1000,2000]
       }
row_label2=['r1','r2','r3','r4','r5','r6','r7','r8']
df=pd.DataFrame(techn2, index=row_label2)
df

#######select rows by index labels
df2=df.loc['r2']    #select r2 by index label
df2
#
df2=df.loc[['r2','r3','r6']]     #select r2,r3,r6 by index label
df2
#
df2=df.loc['r1':'r5']
df2
#
df2=df.loc['r1':'r5':2]     #select alternate rows
df2

###### select column using name or index
df2=df['Courses']
df2
#
df2=df[['Courses','Fee','Duration']]
df2

###select multiple columns
df2=df.loc[:,['Courses','Fee','Duration']]
df2
###select random columns
df2=df.loc[:,['Courses','Duration','Fee']]
df2
#select column between two columns
df2=df.loc[:,'Fee':'Discount']
df2
#select column by range duration and thereafter duration
df2=df.loc[:,'Duration':]
df2
#select column by range
#all the column upto duration
df2=df.loc[:,:'Duration']
df2

#############################################
#############################################
#Pandas.DataFrame.query() by example
#Query all rows with courses equal to  spark
df2=df.query("Courses == 'saprk'")
print(df2)
# not equal condition
df2=df.query("Courses != 'saprk'")
print(df2)

"""
Created on Fri May  5 08:16:06 2023

@author: Omsai
"""
techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       'Discount':[1000,2000,3000,0,500,2000,1000,2000]
       }
row_label2=['r1','r2','r3','r4','r5','r6','r7','r8']
df=pd.DataFrame(techn2, index=row_label2)
df
############## Adding Columns
tutors=['Gaurav','Vaibhav','Ketan','Om','ABC','XZY','PQR','ASD']
df2=df.assign(TutorAssigned=tutors)
df2
#
MNC=['A','B','C','D','E','F','G','H']
df2=df.assign(MNC_Com=MNC)
df2
#######################
#Derive new columns from existing columns
df=pd.DataFrame(techn2, index=row_label2)
df
df2=df.assign(Discount_Per=lambda x:x.Fee*x.Discount/100)
print(df2)

#Append columns to existing DataFrame
df
df["MNC_Com"]=MNC
df
#Add new column at the specific location
#df.insert(loc, column, value)
df=pd.DataFrame(techn2, index=row_label2)
df
df.insert(0,'Tutors', tutors)
df

########################################
########################################
import pandas as pd
import numpy as np

techn2={
       'Courses':['saprk','PySpark','Hadoop','Python','Pandas',None,'DBMS','ADS'],
       'Fee':[200000,100000,300000,5000,100000,np.nan,290000,50000],
       'Duration':['30days','60days','100days','100days','10days','20days','30days','100days'],
       'Discount':[1000,2000,3000,0,500,2000,1000,2000]
       }
row_label2=['r1','r2','r3','r4','r5','r6','r7','r8']
df=pd.DataFrame(techn2, index=row_label2)
df

#Rename column name
df2=df.rename(columns={'Courses':'Courses_List'})
print(df2)
#Alternatively you can also write above code by using axis
df2=df.rename({'Courses':'Courses_List','Fee':'FEE'},axis=1)
print(df2)
#
df2=df.rename({'Courses':'Courses_List'},axis='columns')
print(df2)
#In order to change existing dataframe without copying to existing dataframe
df.rename({'Courses':'Courses_List'},axis='columns',inplace=True)
print(df)


"""
Created on Mon May  8 08:17:32 2023

@author: VAIBHAV BHORKADE
"""

import pandas as pd
lang={
      'Courses':['spark','py','hadook','python','pandas',None,'spark','java'],
      'Fee':[20,23,34,45,56,45,34,34],
      'Duration':[1,2,3,4,5,6,7,8],
      'Discount':['2days','3days','4days','1day','2day','4days','5days','6days']
      } 
row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(lang,index=row_label)
df
#Quick Example of Get the no. pf rows in DataFrame
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count

col_count=len(df.axes[1])
col_count

# 
rows_count=df.shape[0]
rows_count

col_count=df.shape[1]
col_count

#########------ Apply method on column 
import pandas as pd

data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2

##########---------apply on single column 
import pandas as pd

data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
print(df)

def add_5(x):
    return x+5
df['B']=df['B'].apply(add_5)
df['B']

# For two columns 0r multiple columns
def add_5(x):
    return x+5
df[['A','B']]=df[['A','B']].apply(add_5)
df

##############---------Apply lambda fun to each column 
df2=df.apply(lambda x:x+10)
df2

#######################################
# Apply lambda function to single column;'
df["A"]=df["A"].apply(lambda x:x-1)
df

# Instead apply one more fun transform
def add_2(x):
    return x+2
df2=df.transform(add_2)
df2

# map function
df["A"]=df["A"].map(lambda x:x/2)
df

#Using numpy function on single column

import numpy as np
df["A"]=df["A"].apply(np.square)
df

# Using square() method
df['B']=np.square(df['B'])
print(df)

#pandas groupby() with example
import pandas as pd 
techn=({
    "A":['a','b','c','a','b','c','d'],
    "B":[12,32,32,43,545,323,65],
    "C":['1','2','3','4','2','3','3'],
    "D":[12,32,32,43,545,323,65]})
df=pd.DataFrame(techn)
df
# use groupby
df3=df.groupby(['A']).sum()
df2
# multiple column
df2=df.groupby(['A','C']).sum()
df2

# Add index to the group data
df2=df.groupby(['A','C']).sum().reset_index()
df2

##########################################
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']}


"""
Created on Mon May  8 16:50:37 2023

@author: Omsai
"""
import pandas as pd
import numpy as np
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']}
df=pd.DataFrame(technologies)
print(df)
df.columns
#get the list of all column names from headers
column_header=list(df.columns)
column_header

#using list(df) to get the list of all column names
column_header=list(df)
print(column_header)

###############################
###############################
#pandas Shuffle DataFrame Rows
import pandas as pd
import numpy as np
tec={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']}
df=pd.DataFrame(tec)
print(df)

#pandas Shuffle DataFrame Rows
df1=df.sample(frac=1)
print(df1)

# shuffle rows 50 %
df1=df.sample(frac=0.5)
print(df1)

#Create a new Index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)

#Drop shuffle index (Remove previous index)
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)

"""
Created on Tue May  9 08:15:46 2023

@author: Omsai
"""
###  Joining  ###
tec={
    'Courses':['spark','Pyspark','Python','Pandas'],
    'Fee':[2323,3445,6767,3423],
    'DUration':['30days','50days','30days','2days']
    }
row_label=['r1','r2','r3','r4']
df1=pd.DataFrame(tec,index=row_label)
df1

tec2={
    'Courses':['spark','oop','java','spark'],
    'Fee':[2323,3445,6767,3423]
    }
row_label2=['r1','r6','r3','r5']
df2=pd.DataFrame(tec2,index=row_label2)
df2

#pandas join , by  default it will join the table left join
df3=df1.join(df2,lsuffix="_Left",rsuffix="_right")
print(df3)

#pandas inner join DataFrame
df3=df1.join(df2,lsuffix="_Left",rsuffix="_right",how="inner")
print(df3)

#pandas left join DataFrame
df3=df1.join(df2,lsuffix="_Left",rsuffix="_right",how="left")
print(df3)

#pandas right join DataFrame
df3=df1.join(df2,lsuffix="_Left",rsuffix="_right",how="right")
print(df3)

"""
Created on Tue May  9 16:15:14 2023

@author: Omsai
"""
import pandas as pd
import numpy as np
tec={
    'Courses':['spark','Pyspark','Python','Pandas'],
    'Fee':[2323,3445,6767,3423],
    'DUration':['30days','50days','30days','2days']
    }
row_label=['r1','r2','r3','r4']
df1=pd.DataFrame(tec,index=row_label)
df1

tec2={
    'Courses':['spark','oop','java','spark'],
    'Feeg':[2323,3445,6767,3423]
    }
row_label2=['r1','r6','r3','r5']
df2=pd.DataFrame(tec2,index=row_label2)
df2
#pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
print(df3)
 
## using Dataframe.merge()
## inner join
df3=pd.merge(df1, df2)
print(df3)

#
df3=df1.merge(df2)
df3

#using pandas.concat() two DataFrame
data=[df1,df2]
df3=pd.concat(data)
df3

####################################
#concat multiple DataFrame
tec={'Courses':['spark','Pyspark','Python','Pandas'],
    'Fee':[2323,3445,6767,3423],
    'DUration':['30days','50days','30days','2days']}
row_label=['r1','r2','r3','r4']
df1=pd.DataFrame(tec,index=row_label)
df1

tec2={
    'Courses':['spark','oop','java','spark'],
    'Feeg':[2323,3445,6767,3423]
    }
row_label2=['r1','r6','r3','r5']
df2=pd.DataFrame(tec2,index=row_label2)
df2

tec3={'Discount':[2323,3445,6767,3423],
    'DUration':['30days','50days','30days','2days']}
row_label=['r1','r2','r3','r4']
df3=pd.DataFrame(tec3,index=row_label)
df3

df4=pd.concat([df1,df2,df3])
df4
#create csv file using DataFrame
df4.to_csv("c:/Gaurav/courses.csv")

cd=pd.read_csv('courses.csv')
print(cd)

#convert to exel file
cd.to_excel("c:/Gaurav/courses.xlsx")
#read excel file
df0=pd.read_excel("c:/Gaurav/courses.xlsx")
print(df0)





