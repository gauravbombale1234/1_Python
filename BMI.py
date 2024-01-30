# -*- coding: utf-8 -*-
"""
TEST CASE 1:
    write a python code to calculate BMI(Body Mass Index)
    of a person using if elif else
Created on Wed Apr  5 16:47:48 2023

@author: Omsai
"""
"""
height = float(input("Enter the height in m : "))
weight = float(input("Enter the weight in kg: ")) 

BMI=round((weight/(height*height)),2)
 
if BMI<18.5:
    print(f"you are under weight and your BMI is : {BMI}")
elif BMI>18.5 and BMI<25:
    print(f"you are normal weight and your BMI is : {BMI}")
elif BMI>25 and BMI<30:
    print(f"you are over weight and your BMI is : {BMI}")
elif BMI>30 and BMI<35:
    print(f"you are obese and your BMI is : {BMI}")
elif BMI>35:
    print(f"you are clinically obese and your BMI is : {BMI}")
"""

"""
write python code using logical operators and if-elif.
so as so to allow for roller coster also ask user age and 
chargr ticket accordingly
h>120:eligible
    input age
    bill=0
    if age < 12 : ticket is 5$
    elif  12 to 18   ->7
    18 to 45 -> 12
    45 to 55 -> 50

    want photo or not if yes add 3$ in bill 
"""

h=float(input("Enter the height in cm : "))

if (h>120):
    print("You are eligible for this game. ")
    age=int(input("Enter your age"))
    bill=0
    
    if age<12:
        print("your ticket is 5$. ")
        bill=5
    elif age>12 and age<18:
        print("your ticket is 7$.")
        bill=7
    elif age>=18 and age<45:
        print("your ticket is 12$.")
        bill=12
    elif age>=45 and age<55:
        print("your ticket is 50$.")
        bill=50
    else:
        print("your ticket is 60$.")
        bill=60
    k=input(("Do you want photo "))
    if(k=='y' or k=='Y'):
        print("photocopy is ready")
        bill = bill + 5
        print("your final bill is ",bill)




