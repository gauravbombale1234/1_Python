# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:20:36 2023

@author: Omsai
"""
########################################
### Series
# series is used to model one dimensional data and
# DataFrame is used to model two dimensional data
## similar to list in python
import pandas as pd 
songs=pd.Series([145,123,23,13],name='counts')
print(songs)
#range of series
songs.index


"""
Created on Wed May 10 08:29:47 2023

@author: Omsai
"""
#we can also assign string index
songs2=pd.Series([145,123,23,13],name='counts',
    index=['paul','john','george','ringo'])
songs2.index
print(songs2)

# The NaN value 
# this value stands for Not A Number

#Numpy array
import numpy as np 
numpy_ser=np.array([123,23,45,56])
#Mean value of songs2
songs2.mean()

#series with duplicat index
george=pd.Series([10,7,1,22],
        index=['1969','1960','1970','1970'],
        name='George Songs')
print(george)

# read or select the data from a series
george['1960']
george['1970']
# 
for item in george:
    print(item)

# Update the value in series
george['1960']=223
george['1960']

# Delete the value 
s=pd.Series([2,3,4,5],index=[1,2,3,4])
print(s)
del s[1]
print(s)

########## Convert types
#string use astype(str)
#numeris use pd.to_numeric
# integer use astype(int)
# datetime use pd.to_datetime

songs_23=pd.Series([3,None,10,9],
    index=['George','Ringo','John','Paul'],
    name='counts')
# error
pd.to_numeric(songs_23.apply(str))
#ignore the error in above code
pd.to_numeric(songs_23.apply(str),errors='coerce')

"""
Created on Wed May 10 14:48:41 2023
@author: Omsai
"""
songs_23=pd.Series([3,None,10,9],
    index=['George','Ringo','John','Paul'],
    name='counts')

#the NaN Values can be dropped from the 
#series using dropna
songs_23.dropna()

#Append , combining and joinnig two series
songs_60=pd.Series([7,8,2,10],
    index=['A','B','C','D'],
    name='Counts')

songs=songs_23.append(songs_60)
print(songs)


###########################
###########################
# Plotting two series
import matplotlib.pyplot as plt
fig=plt.figure() 
songs_60.plot()
plt.legend()

#############
fig=plt.figure()
songs_60.plot(kind='bar')
songs_23.plot(kind='bar',color='k',alpha=.5)
plt.legend()

############### Histogram
data=pd.Series(np.random.randn(500),
    name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

####################################################
###############   Numpy   ##################
####################################################
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
#datatype of item in array
arr1.dtype

# Multidimesional Array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

## ndmin : Minimum Dimensions
arr=np.array([10,20,30],ndmin=2)
print(arr)

## change the data type
# Change to the complex data type
arr=np.array([10,20,30],dtype=complex)
print(arr)

### Get the dimensions of array
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr.ndim)
print(arr)

# Finding the size of each item in the array
arr=np.array([10,20,30])
print("Each item contain in bytes : ",arr.itemsize)

# data type of each item in the array
arr=np.array([10,20,30])
print("data type is : ",arr.dtype)

# get the shape and size of array
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("size is : ",arr.size)
print("shape is : ",arr.shape)

# array with float data type
arr=np.array([[10,20,30],[40,50,60],[70,80,90]],dtype='float')
print("array created by using list : \n",arr)


# create a sequence of int using arange()
# create a sequence of int from 0 to 20 with steps of 3
arr=np.arange(0,20,3)
print("a sequence of int from 0 to 20 with steps of 3 : \n",arr)

# 
arr=np.arange(11)
print(arr)
print(arr[2])
print(arr[-1])

# Acess multidimensional array using index
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr)
print(arr[1,1])
print(arr[1])
print(arr[-1,-2])
print(arr[1,-1])

# Array Slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[1:8:2])
print(arr[-2:3:-1])
print(arr[-2:10])

#Multidimensional array
arr=np.array([[10,20,30,4],[40,50,60,7],[70,80,90,2],[30,50,20,3]])

print(arr[1,2]) #to access the value at row 1 & column 2
print(arr[1,:]) #to access the value at row 1 & all column
print(arr[:,1]) #to access the value at all row & column 1

print(arr[:3, ::2]) #all rows three column ,in all selected rows 

# Integer array indexing 
arr=np.arange(35).reshape(5,7)    # 5 rows and 7 columns
print(arr)

"""
Created on Thu May 11 08:10:56 2023

@author: Omsai
"""
import numpy as np

arr=np.arange(12).reshape(3,4)    # 3 rows and 4 columns
print(arr)
rows=np.array([False,True,True])
wanted_rows=arr[rows, :]
print(wanted_rows)

#
arr=np.array([10,20,30,40])
print("Array : ",arr)
print(type(arr))

#conversion of array to list
list1=arr.tolist()
print("list : ",list1)
print(type(list1))

#
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Array :\n",arr)
lst=arr.tolist()
print("List : ",lst)

## Conversion of List to array
#   1.numpy.array()
#   2.numpy.asarray()
lst=[10,20,30,40]

arr=np.array(lst)
print("Array : ",arr)
print(type(arr))

#
lst=[10,20,30,40]
arr=np.asarray(lst)
print("Array :",arr)
print(type(arr))

# Numpy Array Properties
#   ndarray.shape
#   ndarray.ndim
#   ndarray.itemsize
#   ndarray.size
#   ndarray.dtype

arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr.shape)    #(3, 3)

#reshape  of array
arr=np.array([[10,20,30],[40,50,60]])
print(arr.shape)
arr.shape=(3,2)
print(arr)
#
arr=np.array([[10,20,30],[40,50,60]])
print(arr.shape)
new_arr=arr.reshape(3 ,2)
print(new_arr)

# ndim
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr.ndim)      #2

#Apply Arithmatic operation on array
arr1=np.arange(16).reshape(4, 4)
print(arr1)
arr2=np.array([1,3,5,7])
print(arr2)
add_arr=np.add(arr1,arr2)
print("Addition of array is : ",add_arr)

# substraction
sub_arr=np.subtract(arr1,arr2)
print("Substraction of array is : ",sub_arr)

# Multiplication of array
mul_arr=np.multiply(arr1,arr2)
print("Multiplication of array is :\n",mul_arr)

# Divide 
div_arr=np.divide(arr1,arr2)
print("Division of array is :\n",div_arr)

# Reciprocal of array
array1=np.array([50,10.3,5,1,200])
rep_arr=np.reciprocal(array1)
print("Reciprocal of Array is :\n",rep_arr)

# to operform power operation
arr=np.array([1,2,3,4,5])
pow_arr=np.power(arr,3)
print("After performing power opertion : \n",pow_arr)

#   power operation
arr1=np.array([1,2,3,4,5])
arr2=np.array([2,3,4,5,6])

pow_arr=np.power(arr1,arr2)
print("After performing power opertion : \n",pow_arr)

##########
# mod function
arr1=np.array([7,20,13])
arr2=np.array([3,5,10])

mod_arr=np.mod(arr1,arr2)
print("After performing mod opertion : \n",mod_arr)

"""
Created on Thu May 11 14:52:11 2023

@author: Omsai
"""
import numpy as np

# create an empty array
from numpy import empty

a=empty([3,3])
print(a)

#create zero array
from numpy import zeros
a=zeros([3,3])
print(a)

#create one array
from numpy import ones
a=ones([3,3])
print(a)

########## creat array with vstack
from numpy import array
from numpy import vstack

#
a1=array([1,2,3])
print(a1)
#
a2=array([4,5,6])
print(a2)

#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.dtype)
print(a3.shape)


# hstack
from numpy import array
from numpy import hstack
import numpy as np
a1=array([1,2,3])
print(a1)
#
a2=array([4,5,6])
print(a2)

#vertical stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)

#
data=[[11,22],[33,44],[55,66]]
data=array(data)
print(data)
print(type(data))

print(data[4])      # Error 
print(data[0,])     #*** 0 th row and all column  

"""
Created on Fri May 12 08:17:46 2023

@author: Omsai
"""
from numpy import array 
#split input and output
data=array([[11,22,44],[33,44,66],[55,66,23]])
#seprate the data
X,y=data[:, :-1], data[:, -1]
"""
data[:, :-1] -> all rows & all columns except last column of all rows
data[:, -1]  -> keeping last column except all column(not last column) 
"""
print(X)
print(y)

###############
# broadcast scalar to one dimensional array
# define array
a=array([1,2,3])
print(a)
#define scalar
b=2
print(b)
#broadcast
c=a+b
print(c)

###########################
#vector addition 
a=array([1,2,3])
print(a)
b=array([1,2,3])
print(b)

c=a+b
print(c)

###########################
#vector substraction 
a=array([1,2,3])
print(a)
b=array([1,2,3])
print(b)

c=a-b
print(c)

#########################
#vector L1 norm  :The L1 norm that is calculated as the sum of the absolute values of the vector.
 
from numpy import array 
from numpy.linalg import norm

a=array([1,2,3])
print(a)
#calculate norm 
l1=norm(a,1)
print(l1)

##########################
#vector L2 norm  : The L2 norm that is calculated as the square root of the sum of the squared vector values.
from numpy import array 
from numpy.linalg import norm

a=array([1,2,3])
print(a)
#calculate norm 
l2=norm(a)
print(l2)

#######################
# triangular matrices
from numpy import array
from numpy import tril
from numpy import triu

M=array([[1,2,3],[1,2,3],[1,2,3]])
print(M)
# lower triangular matrix
lower=tril(M)
print(lower)
# upper triangular matrix
upper=triu(M)
print(upper)

###############################
# Diagonal matrix
from numpy import array
from numpy import diag

M=array([[1,2,3],[1,2,3],[1,2,3]])
print(M)
# extract diagonal vector
d=diag(M)
print(d)
# create diagonal matrix from 
D=diag(d)
print(D)

"""
Created on Fri May 12 14:38:48 2023

@author: Omsai
"""
from numpy import array
from numpy import identity
# Identity Matrix
I=identity(3)
print(I)

# Orthogonal Matrix
from numpy.linalg import inv

Q=array([[1,0],[0,-1]])
print(Q)

v=inv(Q)
print(Q.T)
print(v)
# identity equivalence
I = Q.dot(Q.T)
print(I)
########################
# transpose matrix
from numpy import array
# define matrix
A = array([
[1, 2],
[3, 4],
[5, 6]])
print(A)
# calculate transpose
C = A.T
print(C)
##############################
# invert matrix
from numpy import array
from numpy.linalg import inv
# define matrix
A = array([
[1.0, 2.0],
[3.0, 4.0]])
print(A)
# invert matrix
B = inv(A)
print(B)
# multiply A and B
I = A.dot(B)
print(I)
############################
# sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
# create dense matrix
A = array([
[1, 0, 0, 1, 0, 0],
[0, 0, 2, 0, 0, 1],
[0, 0, 0, 2, 0, 0]])
print(A)
# convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
# reconstruct dense matrix
B = S.todense()
print(B)
###################################
from numpy import array
T = array([
[[1,2,3], [4,5,6], [7,8,9]],
[[11,12,13], [14,15,16], [17,18,19]],
[[21,22,23], [24,25,26], [27,28,29]]])
print(T.shape)
print(T)
############################



##################################
##################################
import matplotlib.pyplot as plt

plt.plot([1,3,2,4])
plt.show()

#
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3 for xi in x])
plt.plot(x,[xi/3.0 for xi in x])

plt.show()

### Adding grid
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)       # select all 4 statements
plt.grid(True)
plt.show()

########## Handling Axes (shift the axis)
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)       # select all 5 statements
plt.axis()
plt.axis([0,5,-1,13])
plt.show()

######## Adding labels (like x-axis , y axis)
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

######### Adding title
import matplotlib.pyplot as plt

plt.plot([1,3,2,4])
plt.title("Graph of variance")
plt.show()

########## Adding legends
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,5)
plt.plot(x,x*1.5,label="Normal")       # select all 6 statements
plt.plot(x,x*3.5,label="Fast")
plt.plot(x,x*2,label="Slow")
plt.legend()
plt.show()

#### control color
import matplotlib.pyplot as plt
import numpy as np

y=np.arange(1,3)
plt.plot(y,"y")
plt.plot(y+1, "m")
plt.plot(y+2, "c")

plt.show()

######### Specifying style in multilines plot
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c')
plt.show()

# change the style
y=np.arange(1,3)
plt.plot(y,'--',y+1,'.:',y+2,':')
plt.show()

######### controling markers
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+1,'o',y+2,'D')
plt.show()

### Histogram charts
import matplotlib.pyplot as plt
import numpy as np

y=np.random.randn(1000)
plt.hist(y)
plt.show()

##### Bar Graph
plt.bar([1,2,3],[3,2,5]) # first list -> coordinates of bar graph
plt.show()                # second list -> height of bar graph

############## Scaterred Graph :-
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)
y=np.random.randn(1000)

plt.scatter(x,y)
plt.show()

#### color to scatter graph
size=50*np.random.randn(1000)
colors=np.random.randn(1000)
plt.scatter(x,y,s=size,c=colors)
plt.show()

#### Adding text to
### global minima & global maxima
X=np.linspace(-4, 4,1024)
Y=25*(X+4)*(X+1)*(X-2)
plt.text(-0.5,-0.25,"Background Minimum")
plt.plot(X,Y,c='k')
plt.show()

######################################
######################################

import seaborn as sns
import pandas 
import matplotlib.pyplot as plt

sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()

#computer vision , renforcement learning , NLP


