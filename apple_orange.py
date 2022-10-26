# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 00:40:08 2021

@author: subha
"""
#%%
def countApplesAndOranges(s, t, a, b, apples, oranges):
    range_apple=[]
    range_orange=[]
    no_of_apple=0
    no_of_orange=0
    for distance_apple in apples:
        range_apple.append(distance_apple+a)
    for distance_orange in oranges:
        range_orange.append(distance_orange+b)
    for element_apple in range_apple:
        if element_apple in range(s,t+1):
            no_of_apple=no_of_apple+1
    for element_orange in range_orange:
        if element_orange in range(s,t+1):
            no_of_orange=no_of_orange+1
    print(no_of_apple)
    print(no_of_orange)
#%%
     