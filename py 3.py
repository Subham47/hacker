# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:53:32 2021

@author: subha
"""

#%%
def information():
    fname = input("Enter your first name:")
    lname = input("Enter your last name:")
    fullname = fname + " " + lname
    
    city = input("Enter your district:")
    state = input("Enter the state:")
    city_state = city + ", " + state
    
    print("You are:",fullname)
    print("You live in:",city_state)
#%%
#%%
def absolute(x):
    if x < 0:
        abs_value = -x
    else:
        abs_value = x
    print("Absolute value is:",abs_value)
#%%
def inches_to_feet(inches):
    feet = inches//12
    inch = inches%feet
    print("Equals:",feet,"feet and ",inch,"inches")
#%%
def rocket():
    count = 10
    while count >= 1:
        print(count,end=" ")
        count=count-1
    print()    
    print("BLASTOFF")
#%%
def rocket_new():
    ct=10
    for ct in range(10,0,-1):
        print(ct,end=" ")
    print()
    print("BLASTOFF!")
#%%
        