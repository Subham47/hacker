# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:10:12 2021

@author: subha
"""




list=[[1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
list1=[44, 48, 46, 36]
list2=[48, 37, 41, 37]
    
def selection_():
    big=0
    index_of_big=0
    for i in list1:
        if big<i and i<40:
            big=i
    print(list1.index(big))

