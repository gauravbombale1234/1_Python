# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 08:25:34 2023

@author: Omsai
"""

# anagram program
def are_anagram(str1,str2):
    a=list(str1.replace(""," ").lower())
    b=list(str2.replace(""," ").lower())
    
    if(len(a)!=len(b)):
        return False
    else:
        return(sorted(a)==sorted(b))
    
print(are_anagram("elbow","below"))
print(are_anagram("race","care"))

# sum of list which divisible 5 and 7
lst=[5,7]
lst1=[1,2,5,7,14,55,45,21,49,8,9]

def return_sum(lst):
    sum=0
    for i in range (len(lst)):
        if(lst[i]%5==0 or lst[i]%7==0):
            sum=sum+lst[i]
    return sum
print(return_sum(lst))
print(return_sum(lst1))


#write a function to reverse the sentence
def reverse_word(input):
    if input=="":
        return "You entered wrong input"
    else:
        words=input.split()
        reverse_sen="  ".join(reversed(words))
    return reverse_sen
print(reverse_word("This is india"))
print(reverse_word("I am vaibhav"))


#Return values
def get_formated_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name
musician=get_formated_name('Gaurav', 'Bombale')
print(musician)

#####################
#Return a Dictionary
def return_dictionary(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=return_dictionary('Gaurav', 'Bombale')
print(musician)

####################
#passing a list
def greet_users(names):
    for name in names:
        msg=f"Hello , {name.title()}!"  #{name.title}={name} both are same
        print(msg)
usernames=['gaurav','vaibhav','ketan']
greet_users(usernames)

###################
#Passing multiple arguments to function using *
def friends(*friend):
    print(friend)
friends('Vaibhav','Ketan','Rohit','Shubham')

def friends2(*friend):
    for i in friend:
        print(f"-{i}")
friends2('Vaibhav','Ketan','Rohit','Shubham')

def make_pizza(size,*toppings):
    print(f"the size of pizza is {size}")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(18, 'mashroom','green peppers','extra')

#####################################
########import function##############

#1 way
import pizza as p
p.make_pizza2(122, 'mushroom','green peppers')

#2. way
from pizza import make_pizza2
make_pizza2(122, 'mushroom','green peppers')

###########################################
#year is leap year or not
def leap_or_not(year):
    if (year>0 and year%4==0) or (year%100==0 and year%400==0):
        return True
    else:
        return False
print(leap_or_not(2016))
print(leap_or_not(2000))
print(leap_or_not(2019))

###################################
"""
Generate password between 7 and 10 charcters
"""
from random import randint

shortest=7  #minimum len of password
longest=10   #maximum len of password
Min_Ascii=33
Max_Ascii=126

def random_password():
    randomLength=randint(shortest, longest)
    
    result=" "
    for i in range(randomLength):
        randomChar=chr(randint(Min_Ascii, Max_Ascii))
        """The chr function takes an ASCII code as its
        parameter.It returns a string  containing the character
        with that ASCII code as its result."""
        result=result+randomChar
    return result

print("your random password is : ",random_password())


"""  
write program to find fibbonacy series
"""
def fibbo(n):
    lst=[]
    previous=0
    current=1
    lst.append(current)
    for i in range(n-1):
        previous,current=current,previous+current
        #current=previous+current
        lst.append(current)
    return lst 
print(fibbo(8))

from pizza import *
make_pizza2(122, 'mushroom','green peppers')

from pizza import *
make_pizza2(122, 'mushroom','green peppers')

with open('sample.txt') as file_object:
    context=file_object.read()
print(context)

with open('sample.txt') as file_object:
    context=file_object.read()
print(context.rstrip())

with open('sample.txt') as file_object:
    context=file_object.read()
print(context)

with open('sample.txt') as file_object:
    context=file_object.read()
print(context.rstrip())

with open('C:/Gaurav/sample.txt') as file_object:
    context=file_object.read()
print(context.rstrip())

with open('sample.txt') as file_object:
    context=file_object.read()
    print(context.rstrip())     #rstrip() remove space in the file

with open('C:/Gaurav/sample.txt') as file_object:
    for line in file_object:
        print(line)

with open('C:/Gaurav/sample.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('C:/Gaurav/sample.txt') as file_object:
    for line in file_object:
        print(line)

with open('C:/Gaurav/sample.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('C:/Gaurav/sample.txt') as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())

""""
Random number for lottery 
"""
from random import randrange
MIN_NUM=1
MAX_NUM=49
NUM_NUMS=6
ticket_nums=[]
for i in range(NUM_NUMS):
    rand=randrange(MIN_NUM,MAX_NUM+1)
    ticket_nums.append(rand)
ticket_nums.sort()
for n in ticket_nums:
    print(n,end="")
    print()

############################################
#program to remove outliers
values=[89,105,7,4,12,23]
retval=sorted(values)
def removeOutliers(data,num_outliers):
    retval=sorted(data)
    for i in range(num_outliers):
        retval.pop(-1)
    return retval
removeOutliers(values,2)
    


"""
write a python code that determine whether or not a password
good
"""
def check_password(password):
    has_upper=False
    has_lower=False
    has_num=False
    for i in password:
        if (i>='A' and i<='Z'):
            has_upper=True
        elif (i>='a' and i<='z'):
            has_lower=True
        elif (len(password)>=8):
            has_num=True
    if (has_upper and has_lower and has_num):
        return 'Good Password'
    else:
        return 'Bad Password'

print(check_password('Pass@123'))
print(check_password('pass@123'))


"""
Created on Thu Apr 13 08:22:41 2023

@author: Omsai
"""
#storing file content in another variable
with open('C:/Gaurav/sample.txt') as file_object:
    lines=file_object.readlines()
    pi_string=""
    for line in lines:
        pi_string +=" "+line.rstrip()
    print(pi_string)
    print(len(pi_string))

####################################
with open('C:/Gaurav/sample.txt','w') as file_object:
    file_object.write(" I am a student of SCOE Kopargaon")
    

a=open('C:/Gaurav/sample.txt') 
a.readlines()

###########################################
with open('C:/Gaurav/sample.txt','w') as file_object:
    file_object.write("\n I am a student of SCOE Kopargaon")
    file_object.write(" Gaurav Bombale")

a=open('C:/Gaurav/sample.txt') 
a.readlines()

#######################################
####Append to file  -> does not delete previous data
with open('C:/Gaurav/sample.txt','a') as file_object:
    file_object.write("\n I am a student of SCOE Kopargaon")
    file_object.write(" Gaurav Bombale")

a=open('C:/Gaurav/sample.txt') 
a.readlines()

########################################
########   Exception Handling   ########
########################################
try:
    print(5/0)
except ZeroDivisionError:
    print("\n You can't divide by zero!")

############
print("Give me two numbers and i will divide them")
print("Enter q to quit")

while True:
    first_num=input("Enter 1st number")
    if first_num=='q':
        break
    second_num=input("Enter 2nd number")
    if second_num=='q':
        break
    ans=int(first_num)/int(second_num)
    print(ans)

#####################
try:
    with open('sample2.txt','a',encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
        print("Enter correct file name")

"""
Created on Mon Apr 17 08:29:01 2023

@author: Omsai
"""
#JSON module (Javascript Object Notation)
import  json 
num=[2,3,23,45,67,54,43]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(num, f)

################### for writing in json file
import json
username=input("Enter the name ")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username, f)
print(f"We'll remember you when you come back,{username}")

################### for read the json file
import json
filename='username.json'
with open(filename) as f:
    username=json.load(f)
print(f"welcome back, {username}")

####################
#load the username , if it has been stored previously
#othrwise , prompt for the username and store it
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("Enter the name ")
    with open(filename,'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back,{username}")
else:
    print(f"welcome back , {username}")

#####################
lst2=[]
for i in range(0,20):
    lst2.append(i)
print(lst2)

###########1.List comprehensation##########
##same as for append the element in the list 
lst3=[num for num in range(0,20)]
print(lst3)

##############
names=['gaurav','vaubhav','ketan']
lst=[name.capitalize() for name in names]
print(lst)

###################
#list comprehension with if statement
def is_even(num):
    return num%2==0
lst=[
     num
     for num in range(10)
     if is_even(num)
     ]
print(lst)

"""
Created on Tue Apr 18 08:11:50 2023

@author: Omsai
"""
lst=[
     f"{x}{y}"
     for x in range(3)
     for y in range(3)
     ]
print(lst)

#############
lst=[
     f"{x}{y}"
     for x in range(10)
     for y in range(10)
     ]
print(lst)

###########################
###  2.Set Comprehension  ###
###########################
lst={
     x
     for x in range(3)
     }
print(lst)

###########################
###  3.Dictipnary Comprehension  ###
###########################
Dict1={
     x:x*x
     for x in range(10)
     }
print(Dict1)

#############################
####### Generator ##########
############################
#it is another way to creating iterators
#it uses the keyword 'yield'
#instead of returning it in a defined function , Generators are implemented using a finction

gen=(x
     for x in range(3)
     )
print(gen)
for num in gen:
    print(num)

################next method
gen=(x
     for x in range(10)
     )
next(gen)
next(gen)
next(gen)

#######function which return multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(20):
    print(num)

#################
def range_even(end):
    for num in range(0,end,2):
        yield num
gen=range_even(10)
next(gen)
next(gen)

##################Chaining Generators#########
######code for hiding the password
def lengths(itr):      #for calculating len of password
    for ele in itr:
        yield len(ele)
def hide(itr):          #for hiding the password
    for ele in itr:
        yield ele* '*'

password=['not-good','give-m-pass','98392392']

for password in hide(lengths(password)):
    print(password)

###########printing list with index
lst=['Milk','Egg','Bread']
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")

###################
### password picker
import string

adjective=['sleepy','slow','smelly','wet','fat','red',
           'orange','yellow','green','blue','purple','fluffy',
           'white','proud','brave']

nouns=['apple','dinosour','ball','toaster','goat','dragon',
       'hammer','duck','panda']

import random

adjective=random.choice(adjective)
noun=random.choice(nouns)
#select a number
number=random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
#create the new secure password
password=adjective + noun + str(number) + special_char

print("Your new password is : %s" %password)

#######################
print("welcome to password picker")
while True:
    adjective=random.choice(adjective)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password=adjective + noun + str(number) + special_char
    print("Your new password is : %s" %password)
    response=input("would you like another password ('Y' or 'N')")
    if response == 'N' or response == 'n':
        break
    
########################
adj=[]
nouns=[]   
#for appending adjectives
while True:
    c=input("\n Enter the Adjective : ")    
    adj.append(c)
    response=input("\n Would you like another Adjective ('Y' or 'N') ")
    if response == 'N' or response == 'n':
        break
print("\n")    
print("\n Adjective = ",adj)   
#for appending nouns  
while True:
    c=input("\n Enter the Noun : ")    
    nouns.append(c)
    response=input("\n Would you like another noun ('Y' or 'N') ")
    if response == 'N' or response == 'n':
        break
print("\n")   
print("\n Noun = ",nouns)      
 
import random
import string
   
def check_password(password):
    has_upper=False
    has_lower=False
    has_num=False
    for i in password:
        if (i>='A' and i<='Z'):
            has_upper=True
        elif (i>='a' and i<='z'):
            has_lower=True
        elif (len(password)>=8):
            has_num=True
    if (has_upper and has_lower and has_num):
        return 'Good Password'
    else:
        return 'Bad Password'
    
    
print("\n Welcome to password picker ")
while True:
    adjective=random.choice(adj)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password=adjective + noun + str(number) + special_char
    
    print(f"\n new password is : {password} ")
    print(check_password(password))
    response=input("\n Would you like another password ('Y' or 'N') ")
    if response == 'N' or response == 'n':
        break


"""
Created on Wed Apr 19 08:13:23 2023

@author: Omsai
"""
########Enumerate###############
################################  
lst=['Milk','Egg','Bread']
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")

############Use zip function
name=['Gaurav','Vaibhav','Ketan']
info=[1234,5678,34567]
for nm,inf in zip(name,info):
    print(nm,inf)

##########################
#use of zip function with mis match list
#it will not display extra element i.e. Shubham
name=['Gaurav','Vaibhav','Ketan','Shubham']
info=[1234,5678,34567]
for nm,inf in zip(name,info):
    print(nm,inf)

#########################
###### Zip longest  #####
#########################
from itertools import zip_longest
name=['Gaurav','Vaibhav','Ketan','Shubham']
info=[1234,5678,34567]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

################ use auto fill value for mismatch value in zip_longest function
from itertools import zip_longest
name=['Gaurav','Vaibhav','Ketan','Shubham']
info=[1234,5678,34567]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

#########################
####all() function  ####
# return false if value is 0
#########################
lst=[2,3,6,4,7,8]
if all(lst):
    print("all values are true")
else:
    print("useless")

#############
lst=[2,3,6,4,7,8,0]
if all(lst):
    print("all values are true")
else:
    print("useless")
    
########################
########## any () function#####
##############################
lst=[0,0,0,6,0]
if any(lst):
    print("some values are true")
else:
    print("all values are zero")

################
lst=[0,0,0,0,0]
if any(lst):
    print("some values are true")
else:
    print("all values are zero")

##################################
########## count() ################
##################################
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
 
######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

####################
users=['admin','employee','manager','worker','staff']
for user in users:
    if user=='admin':
        print("Hello admin , would you like to see a status report ")
    elif (user=='employee'):
        print("hello employee")
    elif (user=='manager'):
        print("hello manager")
    elif (user=='worker'):
        print("hello worker")
    else:
        print("hello")

#############
current_users=['Gaurav','Shubham','Vaibhav','Ketan','Rohit']
new_users=['Gaurav','Vaibhav','Sai','Yash','Shree']
for i in new_users:
    if i in current_users:
        print("person will need to enter a new username")
    else:
        print("saying that the username is available ")

#################
import hashlib
hashlib.sha256("Gaurav@1234".encode('utf-8')).hexdigest()
'778d4ce2dfb7063981a67be5ba7955ba063c3319760bd3a0d2a85f5d15a594de'
len(hashlib.sha256("Gaurav@1234".encode('utf-8')).digest())

###############
import hashlib
hashlib.sha512("Gaurav@1234".encode('utf-8')).hexdigest()
'778d4ce2dfb7063981a67be5ba7955ba063c3319760bd3a0d2a85f5d15a594de'
len(hashlib.sha512("Gaurav@1234".encode('utf-8')).digest())

######################################
users=['admin','employee','manager','worker','staff']
password=['Admin@123','Employee@123','Manager@123',
          'Worker@123','Staff@123']
pass_hash_code=[]
count=0

import hashlib
for i in password:
    a=hashlib.sha512(i.encode('utf-8')).hexdigest()
    pass_hash_code.append(a)

def password_checker(): 
    global count
    n=input("\n Enter Password : ")
    n1=hashlib.sha512(n.encode('utf-8')).hexdigest()

    if n1 in pass_hash_code:
        index=password.index(n)
        user2=users[index]
        
        if user2=='admin':
            print("Hello admin , would you like to see a status report ")
        elif (user2=='employee'):
            print("Hello Employee")
        elif (user2=='manager'):
            print("Hello Manager")
        elif (user2=='worker'):
            print("Hello Worker")
        
    else:
        print("\n Access Denied")
        count = count + 1
        print(count)
        
            
while(count<3):
    password_checker()
    
else:
    print("\n You loose your chances ")
    print("\n Try Later ")   
    
"""
Created on Fri Apr 21 08:20:37 2023

@author: Omsai
"""
#######################Pandas : open frame
import pandas as pd
f1=pd.read_csv('C:/Gaurav/buzzers.csv')
print(f1)

########### OS: Raw data
import os
with open('buzzers.csv') as raw_data:
    print(raw_data.read())

############## CSV: Reading CSV Data as Lists
## Display data in list form
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)

############ Reading CSV Data as Dictionary
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)

####################
with open('buzzers.csv') as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights

####################remove \n in above code output
#stripping then splitting , your raw data
with open('buzzers.csv') as data:
    ignore=data.readline()
    flights={}
    for line in data:
        k,v=line.strip().split(',')
        flights[k]=v
flights

#######################
#pre-requisite to decorators
def plus_one(number):
    return number + 1
plus_one(5)

#######################
def plus_one(number):
    
    def add_one(number):
        number1=number+1
        return number1
    
    result=add_one(number)
    return result
plus_one(90)

#####################
#passing functions to Arguments to othr function
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)

#####################
def hello_function():
    def say_hi():
        return 'hii'
    return say_hi
hello=hello_function()
hello()








