# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:34:24 2023

Gaurav Bombale 
Branch : Computer
"""
    
import pandas as pd  

df=pd.read_csv('C:/Gaurav/Data_Science_Attendance_Sheet2.csv')

# Q. 1 Rename column name
df.rename(columns={' Gaurav Bombale':'GauravB'},inplace=True)
print(df)


#Q. 2 Convert your column into list
df=pd.read_csv('C:/Gaurav/Data_Science_Attendance_Sheet2.csv')

list1=list(df[' Gaurav Bombale'])
print(list1)

#Q. 3 From the derived list,find out how for how many days,you appeared 0,1,2,3,4,5,7 sessions
list1.count(0)

list1.count(1)

list1.count(2)

list1.count(3)

list1.count(4)

list1.count(5)

list1.count(7)

# Q.4 Generate a bar graph of your attendance
import matplotlib.pyplot as plt
fig=plt.figure()
df[' Gaurav Bombale'].plot(kind='bar')
plt.legend()

####Q.5 Generate 5 number summary using describe() and illustrate the minimum number of sessions ,max
##number of sessions and mean number of sessions you did during the training
df[' Gaurav Bombale'].describe()


#Q.6 Generate box plot using seaborn for your column and write the inference

import seaborn as sns
sns.boxplot(list1)


# Q.7 Generate joint plot using seaborn for your column and write the inference
import seaborn as sns
sns.jointplot(list1)

## Q. 8 From complete dataframe, find out how many are regular students, how many are moderate and
###how many are poor in attendance.
#def check_Attendance():
    
df2=df[-1: ]
print(df2)

if df2.iloc[-1:] >= 80:
    print(df2.columns,'You are regular')
elif df2.iloc[-1:] > 50:
    print(df2.columns,'You are regular')
else :
    print(df2.columns,'You are regular')
"""
MArksheet.csv
"""
import pandas as pd
mark=pd.DataFrame(pd.read_csv('Marksheet.csv'))
mark

# 9. Out of functions, list and dictionary ,in which area you are strong and weak?
mymarks=mark.iloc[42]
print(mymarks['List'])
print(mymarks['Dictionary'])
if mymarks['List'] > mymarks['Dictionary']:
    print('I am strong in list and weak in dictionary')
else:
    print('I am strong in dictionary and weak in list')
    
#Q.10 How many students have shown very good performance and how many have shown poor
#performance?
count1=0
count2=0
# list of values of 'Marks' column
marks_list = mark['Total'].tolist()
marks_list

for i in range (0,len(marks_list)):
    if(marks_list[i] >=8):
        count1 = count1 + 1
    else:
        count2 = count2 + 1

print('number of students having good performance',count1)
print('number of students having avg performance',count2)

"""
Given the document AI_jobs_in_2024.docx,attempt following questions
"""
#Q.11 Open the given file in read mode
file = open("AI_jobs_in_2024.docx", "r")
print(file)
#Q.12 Remove the numbers from the text
obj = open("C:/Gaurav/AI_2024.txt" , "r")
obj.read()

import re

def remove_numbers(text):
    result = re.sub(r'\d+', '' , text)
    return result

txt = " "  
for line in "AI_jobs_in_2024.txt":
    txt = txt + obj.readline()
print(txt)

remove_numbers(txt)


pattern = r'[0-9]'

# Match all digits in the string and replace them with an empty string
new_string = re.sub(pattern, '', string1)

print(new_string)


# .16 Convert numbers into words
import inflect
p=inflect.engine()
def convert_number(text):
    temp_str=text.split()
    new_string=[]
    for word in temp_str:
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)
    temp_str=' '.join(new_string)
    return temp_str
a=12
convert_number(a)
convert_number(3)