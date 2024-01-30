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

#3.way
from pizza import *
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
    lst=[0]
    previous=0
    current=1
    lst.append(current)
    for i in range(n-1):
        previous,current=current,previous+current
        lst.append(current)
    return lst 
print(fibbo(10))


"""
Created on Wed Apr 12 08:35:50 2023

@author: Omsai
"""
from pizza import *
make_pizza2(122, 'mushroom','green peppers')

"""
File Handling
"""
####### Relative path  ##########
with open('sample.txt') as file_object:
    context=file_object.read()
print(context)

#########
with open('sample.txt') as file_object:
    context=file_object.read()
print(context.rstrip())     #rstrip() remove space in the file

######### Absolute Path  ##############
with open('C:/Gaurav/sample.txt') as file_object:
    context=file_object.read()
print(context.rstrip()) 

######## Read file line by line #########
with open('C:/Gaurav/sample.txt') as file_object:
    for line in file_object:
        print(line) 

########
with open('C:/Gaurav/sample.txt') as file_object:
    for line in file_object:
        print(line.rstrip()) 

##########
with open('C:/Gaurav/sample.txt') as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())

"""
Random number for lottery
"""
from random import randrange
min_num=1
max_num-49
num_num=6
ticket_nums=[]
for i in range(num_num):
    rand=randrange(min_num,max_num+1)
    while rand in ticket_nums:
        rand=randrange(min_num,max_num+1)
    ticket_nums.append(rand)
ticket_nums.sort()
for n in ticket_nums:
    print(n,end="")
    print()












