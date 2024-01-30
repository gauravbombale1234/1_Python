# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:25:51 2023

@author: Omsai
"""

def make_pizza2(size,*toppings):
    print("we are in pizza.py file")
    print(f"the size of pizza is {size}")
    for topping in toppings:
        print(f"-{topping}")

