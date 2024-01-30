# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:17:40 2023

@author: Omsai
"""

##### Advanced Python  ###########
## Decorators
#prerequisites

def plus_one(number):
    number1=number+1
    return number1

plus_one(5)

####
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result

plus_one(6)

### passing function as argument
def plus_one(number):
    number1=number+1
    return number1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)

#### function returning other function(object is created when calling)
def hello_function():
    def say_hi():
        return 'Hi'
    return say_hi

hello=hello_function()
hello()

#########
###python decorator is a function that takes in a function
###and returns it by adding some functionality
def say_hi():
    return 'Hi Gaurav'

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper()

decorate=uppercase_decorator(say_hi)
decorate

#######
'''use below code other than above'''
@uppercase_decorator
def say_hi():
    return 'Hi Gaurav'

say_hi

#### applying multiple decorators to a single function

def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
@split_string
@uppercase_decorator
def say_hi():
    return 'hi there'

say_hi()


####
numbers=[2,6,7,8]
def cal_square(numbers):
    result=[]
    for i in numbers:
        result.append(i*i)
    return result
def cal_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i)
    return result
print(cal_square(numbers))
print(cal_cube(numbers))


#####
import time
def cal_square(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i)
    
    end=time.time()
    print((end-start)*1000)
    print("took"+str((end-start)*1000) + "mil sec")
    return result

def cal_cube(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i*i)
    
    end=time.time()
    print((end-start)*1000)
    print("took"+str((end-start)*1000) + "mil sec")
    return result

array=range(1,100000)
out_square=cal_square(array)  
out_cube=cal_cube(array)

###############
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__ + " took "+ str((end-start)*1000)+ "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,100000)
out_square=calc_square(array)  
out_cube=calc_cube(array)

"""
Created on Sat Jun 10 08:13:23 2023

@author: Omsai
"""
####### Shallow copy and Deep copy  #########
'''In python , assignment statements (obj_b=obj_a) do not create real copies.
It will only create new variable with same reference.
'''


#This will only create a new variable with the sa,e reference. 
#Modifying one will affect the other.
list_a=[1,2,3,4,5]
list_b=list_a

list_a[0]=-10
print(list_a)       #[-10, 2, 3, 4, 5]
print(list_b)       #[-10, 2, 3, 4, 5]

####### shallow copy
'''one level deep . Modifying on level 1 does not affect the other list
use copy.copy()
'''
import copy 

list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

#no affects the other list
list_a[0]=-10
print(list_a)       #[-10, 2, 3, 4, 5]
print(list_b)       #[1, 2, 3, 4, 5]

##################
#But with nested objects, modifying on level 2 or deeper does not affect the other
import copy 

list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affects the other list
list_a[0][0]=-10
print(list_a)       #[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(list_b)       #[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]] 

################
### Deep copies
# Full independent clones. use copy.deepcopy()

import copy 

list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#not affects the other list
list_a[0][0]=-10
print(list_a)       #[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(list_b)       #[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

##################














