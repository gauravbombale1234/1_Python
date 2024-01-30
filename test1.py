# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:51:25 2023

@author: Admin
"""
'''
Q.1
Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

'''

import pandas as pd 
import numpy as np
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
            }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df=pd.DataFrame(exam_data)
df

df['qualify'].replace('yes','True')
df

'''
Q2Write a Python program to plot two or more lines  with different styles. 
'''
import matplotlib.pyplot as plt

plt.plot([1,3,2,5,3],'--')
plt.plot([6,3,7,4,2],'-')
plt.show()


'''Q.3 Create an array[1,2,3] write L1 and L2 norm value for it'''
import numpy as np

array=np.array([1,2,3])
array

'''
Q.4 Write a NumPy program create [[1, 0], [1, 2]] square array and  
compute the determinant of a given square array.
'''
array2=np.array([[1, 0], [1, 2]])
array2
print(np.linalg.det(array2))
'''
Q.5 Write a Python function to find the kth smallest element in a list.
'''

def find_smallest(lst,k):
    lst2=[]
    lst2=(sorted(l1))
    return (lst2[k-1])

l1=[34,2,67,453,653,87,1]
print(find_smallest(l1,2))




