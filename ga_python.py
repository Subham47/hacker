# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:36:01 2021

@author: subha
"""

#import sys
import random
#%%
profit=(2,3,6,9,8,15,1,18,19,20)
weight=(8,9,2,4,1,5,7,17,19,12)
#%%
list=[[1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
list1=[44, 48, 46, 36]
list2=[48, 37, 41, 37]
#%%
import random
def random_():
    list=[]
    random.seed(99)
    for i in range(4):
        list.append([])
        for j in range(10):
            list[i].append(random.randint(0,1))
    print(list)
#%%
def fitness_():
    tp=0
    tw=0
    list1=[]
    list2=[]
    for i in range(4):
        for j in range(10):
            tp=tp+list[i][j]*profit[j]
            tw=tw+list[i][j]*weight[j]
        list1.append(tp)
        list2.append(tw)
        tp=0
        tw=0
    print(list1)
    print(list2)
#%%
def selection_():
    big=0
    big=max(list1)
    for i in range(len(list1)):
        if big==list1[i]:
            index_of_big=i
    return list1[index_of_big]
#%%    
def main_():
    
    random_()
    fitness_()
    print("Best individual is",selection_())
    
if __name__ == '__main__':
    main_()
#%%
def crossover_():
    point_of_crossover=4
    for i in range(0,4,2):
        for j in range(point_of_crossover+1):
            if i+1<len(list):
                temp=list[i][j]
                list[i][j]=list[i+1][j]
                list[i+1][j]=temp
#%%
def mutation_():
    for i in range(4):
        for j in range(4,7):
            if list[i][j]==0:
                list[i][j]=1
            else:
                list[i][j]=0
    return (list)
#%%