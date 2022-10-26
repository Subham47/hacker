# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:04:54 2021

@author: subha
"""


"""
Exercise:
Write a function 'def areatriangle(b,h)' to compute the area
of a triangle: formula is area = .5*b*h.
Output should look like:
The area of a triangle of base 3 and height 5 is 7.5

You can test your function by executing the following code:
"""
#%%
# The following will test areatriangle()
areatriangle(3,5)
areatriangle(2,20)
#%%
"""
Solution:
"""
#%%
def areatriangle(b,h):
    area = .5 * b * h;
    print("The area of triangle of base",b,"and height",h,"is",area);    
 
#%%
#%%
def celsiustofahrenheit(temp):
    celsius = (9/5)*temp + 32;
    print("The temprature in fahrenheit is",celsius,end='')
    print(" that's it")
#%%

