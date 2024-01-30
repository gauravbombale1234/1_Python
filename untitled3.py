# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:34:55 2023

@author: Omsai

  
"""
#write progran to get numpy verson
import numpy as np
np.__version__

np.show_config() 

#add function
np.info(np.add)

#transpose
np.transpose

#test whether none of the element are zero
x=np.array([1,2,34,4])
np.all(x)

#
x=np.array([1,2,34,0])
np.all(x)

# Test any of element is non zero
x=np.array([0,0,23,0])
x
np.any(x)

# test for finite set
a=np.array([1,0,np.nan,np.inf])

np.isfinite(a)

import numpy as np
#check the number is complex or not
a=np.array([1+2j,1+0j,22])
print(a)

print("checking for complex number")
print(np.iscomplex(a))

print("checking for real number")
print(np.isreal(a))

print("checking for scalar number")
print(np.isscalar(3.1))

a=[[11,12,13],[21,22,23],[311,32,33]]
A=np.array(a)
A
A.ndim

A.shape
A.size

#access elements of matrix
A[1,2]
A[1][2]

A[0][0]
A[0][0:2]
A[0:3][0:2]
A[:1,2]

###########
x=np.array([[2,1],[2,4]])
y=np.array([[1,2],[3,4]])

z=x+y
z

z=x*y
z
#
z=np.dot(x,y)
z
#calculate the sine of a
np.sinc(z)

#transposed of matrix
x=np.array([[1,1],[2,2],[3,3]])
x

x.T

"""
Created on Thu Jun  1 08:17:27 2023

@author: Omsai
"""
import numpy as np

a=np.array([1+2j,2+5j,2,3.4,43])
print(np.iscomplex(a))

#
p=np.array([[2,1],[2,4]])
q=np.array([[1,2],[3,4]])

result1=np.dot(p,q)
print('Multiplication of matrix ',result1)
########### Outer Product
result2=np.outer(p,q)
print('outer product of matrix \n',result2)

### Cross product
result3=np.cross(p,q)
result4=np.cross(q,p)

print('Cross Product is \n',result3)
print('Cross Product is \n',result4)

##### Determinent of matrix
from numpy import linalg as la
print('Determinent of matrix is',np.linalg.det(p))

# Eigin Value and Eigin vector


import numpy as np
m=np.mat("3 -2;1 0")
print("Original Matrix: ",m)
w,v=np.linalg.eig(m)
print("Eigenvector of the said matrix",w)

print("Eigenvalue of the said matrix",v)

# Inverse of matrix

import numpy as np
m=np.array([[1,2],[3,4]])
m
result=np.linalg.inv(m)
print("Inverse of matrix",result)

# Normal Distrubustion
# Generate 5 numbers

x=np.random.normal(size=5)
print(x)

# Genetrate 6 random no bet

x=np.random.randint(low=10,high=30,size=6)
print(x)

# Random 3*3*3 array values

x=np.random.random((3,3,3))
x

# 5 * 5 array with max and min value

x=np.random.random((5,5))
x
xmin,xmax=x.min(),x.max()
print(xmin,xmax)

"""
Created on Fri Jun  2 08:18:27 2023

@author: Omsai
"""
import numpy as np
#Maximum & Minimum value along the second axis
x=np.arange(4).reshape((2,2))
print(x)
print("\nMaximum value along the second axis : ")
print(np.amax(x,1))

print("\nMinimum value along the second axis : ")
print(np.amin(x,1))
 
##### write program to draw suitable line with x axis ,y axis and a title
import  matplotlib.pyplot as plt
x=range(1,50)
y=[value *3 for value in x]
print("values of x ")
print(*range(1,50))
print("values of y (thrice of x) ")
print(y)
#plot lines and / or markers to the axis
plt.plot(x,y)
plt.xlabel('x axis')    # adding x axis label 
plt.ylabel('y axis')     # adding y axis label 
plt.title("plot of line")
plt.show()

###################### plot graph of given values of x and y
x=[1,2,3]
y=[2,3,1]

plt.plot(x,y)
plt.xlabel('x axis')    # adding x axis label 
plt.ylabel('y axis')     # adding y axis label 
plt.title("plot of line")
plt.show()

###############
import pandas as pd

df=pd.read_csv('C:/Gaurav/fdata.csv')
df.plot()
plt.show()

#########
df=pd.read_csv('C:/Gaurav/Data_Science_Attendance_Sheet2.csv')
df

df2=df.drop('year',axis=1)
df2=df.drop('month',axis=1)
df2=df.drop('weekday',axis=1)
df2=df.drop('datum',axis=1)

df2=df2[:-1]
df2.plot()
plt.show()

"""
Created on Sat Jun  3 08:22:57 2023

@author: Omsai
"""
import numpy as np
import  matplotlib.pyplot as plt

# more legends , different width and color
x1=[10,20,30]
y1=[20,40,10]
x2=[10,20,30]
y2=[40,10,20]

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title('different width and color')
plt.plot(x1,y1, color='blue',linewidth=3,label='line1' )
plt.plot(x2,y2, color='red',linewidth=5,label='line2' )

plt.legend()
plt.show()

#####two or more line with different styles
x1=[10,20,30]
y1=[20,40,10]
x2=[10,20,30]
y2=[40,10,20]

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title('different width and color')
plt.plot(x1,y1, color='blue',linewidth=3,label='line1',linestyle='dotted' )
plt.plot(x2,y2, color='red',linewidth=5,label='line2',linestyle='dashed' )

plt.legend()
plt.show()

######## two or more lines and set line markers
x=[1,4,5,6,7]
y=[2,6,3,6,3]

plt.plot(x,y, color='red',linewidth=3,label='line1',linestyle='dashdot',marker='o',
         markerfacecolor='blue',markersize=12)

#set y limitd
plt.ylim(1,8)
#set x limitd
plt.xlim(1,8)

plt.title('Display marker')
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.legend()
plt.show()

######### several lines with different formsts in one command
import numpy as np
import  matplotlib.pyplot as plt
#sampled time at 200ms intervals
t=np.arange(0.,5.,0.2)

#green dashes , blue squares and red triangles
plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
plt.show()

###### display bar charts of popularity of programming languages
x=['Java','Python','PHP','Javascript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title('bar charts of popularity of programming languages')
plt.xticks(x_pos,x)
plt.show()

####### horizontal bar graph
x=['Java','Python','PHP','Javascript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title('bar charts of popularity of programming languages')
plt.yticks(x_pos,x)
plt.show()

######create bar plot by group and gender
n_groups=5
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)

#create plot
fig,ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8

rects1=plt.bar(index,men_means,bar_width,
               alpha=opacity,color='g',label='men')

rects2=plt.bar(index + bar_width,women_means,bar_width,
               alpha=opacity,color='r',label='women')

plt.xlabel("Person")
plt.ylabel("Scores")
plt.title('Scores by person')
plt.xticks(index + bar_width,('G1','G2','G3','G4','G4'))
plt.legend()
plt.tight_layout()
plt.show()

"""
Created on Tue Jun  6 08:22:37 2023

@author: Omsai
"""
from PyPDF2 import PdfFileReader
# importing required modules
from PyPDF2 import PdfReader

#creating a pdf reader object
reader=PdfReader('c:/Gaurav/OSA_report.pdf')

#printing number of pages in pdf file
print(len(reader.pages))

#getting a specific page from the pdf file
page=reader.pages[0]

#extracting text from page
text=page.extract_text()
print(text)

################################3
import re
chat2='Hi:  I have a problem with my order number 2834798'
pattern='order[^\d]*'


"""
Created on Wed Jun  7 08:16:53 2023

@author: Omsai
"""
'''
re expression
\d\d\d\d\d  -> for 5 digit
\d{10}   -> for 10 digit
'''
import re 
text1="My mobile number is 1234567898"
text2="My alternative mobile number is 8765445678"
text3="My international mobile number is (123)-456-79898"

pat1='\d{10}'
mob_num=re.findall(pat1,text1)
mob_num

pat2='\(\d{3}\)-\d{3}-\d{5}'    # for text3
mob_num2=re.findall(pat2,text3)
mob_num2

###################  Find Email
text1="My email id is gaurav@gmail.com"
text2="My another email id is gaurav_BOM@gmail.com"
text3="My official email id is gaurav123@gmail.com"

pat3="[a-z_A-Z0-9]*@[a-z]*\.com"
email1=re.findall(pat3,text1)
email1

email2=re.findall(pat3,text2)
email2

email3=re.findall(pat3,text3)
email3

#########
text4="My email id is gaurav.bombale@sanjivani.org.in"
pat4="[a-z_A-Z0-9\.]*@[a-z]*\.org\.in"

email4=re.findall(pat4,text4)
email4

###########
chat1="Hi my order #45797 is not received yet"
chat2="Hi i having problem with order number 46765765 which is not received yet"

patt="order[^\d]*(\d*)"

te=re.findall(patt,chat1)
te

te2=re.findall(patt,chat2)
te2

#############
chat1="Hi my order #45797 is not received yet"

def get_pattern_matches(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches

get_pattern_matches('order[^\d]*(\d*)', chat1)

######### 
chatt1='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and chairman of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp. and X.AI
Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​   
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[a][3]'''

get_pattern_matches(r'age (\d+)', chatt1)

match=get_pattern_matches(r'Born(.*)', chatt1)
print(match[0].strip())

###
get_pattern_matches(r"Born.*\n(.*)\(age", chatt1)

###
def extract_personal_information(text):
    age=get_pattern_matches('age (\d+)', text)
    full_name=get_pattern_matches('Born(.*)\n', text)
    birth_date=get_pattern_matches('Born.*\n(.*)\(age', text)
    birth_place=get_pattern_matches('\(age.*\n(.*)', text)
    return{
        'age': age,
        'name': full_name,
        'birth place': birth_place,
        'birth date': birth_date
        }

extract_personal_information(chatt1)

########
text12='''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''

extract_personal_information(text12)

######
#1. extract all twiter handles from following test
text='''Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''

pattern='https://twitter.com/([a-zA-Z0-9_]+)'

get_pattern_matches(pattern, text)
#or
re.findall(pattern, text)

#########
#2. extract 
text='''Concentration of Risk: Credit Risk 
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021 and December 31,'''

pattern='Concentration of Risk: ([^\n]*)'

re.findall(pattern,text)

################### find the year
text='''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'

matches=re.findall(pattern,text)
matches

############# extract phone numbers
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. 
Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777
'''
pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches=re.findall(pattern, text)
matches

##########################
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern='Note \d - ([^\n]*)'
matches=re.findall(pattern, text)
matches

####################
#extract financial period from companys financial report
text = """
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
"""
pattern='FY\d{4} Q[1-4]'

matches=re.findall(pattern, text)
matches

################# finding case insensitive words
text = """
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. fy2020 Q4 it was $3 billion.
"""

pattern='FY\d{4} Q[1-4]'

matches=re.findall(pattern, text,flags=re.IGNORECASE)
matches

###### extract only financial numbers
text = """
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
"""

pattern='\$([0-9\.]+)'   # $ is necessary in pattern 

matches=re.findall(pattern, text)
matches










