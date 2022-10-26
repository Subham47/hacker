# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:04:12 2021

@author: subha
"""
grades=[73,67,38,33]

def gradingStudents(grades):
    list=[]
    for element in grades:
        n=element
        if n>=38:
            while n%5!=0:
                n=n+1
            if n-element<=2:
                element=n
        list.append(element)
    print(list)