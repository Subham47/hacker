# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:20:40 2021

@author: subha
"""
import random

profit=(2,3,6,9,8,15,1,18,19,20)
weight=(8,9,2,4,1,5,7,17,19,12)

def random_():
    list=[]
    #random.seed(99)
    for i in range(64):
        list.append([])
        for j in range(10):
            list[i].append(random.randint(0,1))
    return list
    
def fitness_(list):
    tp=0
    tw=0
    list1=[]
    list2=[]
    for i in range(64):
        for j in range(10):
            tp=tp+list[i][j]*profit[j]
            tw=tw+list[i][j]*weight[j]
        list1.append(tp)
        list2.append(tw)
        tp=0
        tw=0
    return(list1,list2)

def selection_(list1):
    big=0
    for i in list1:
        if big<i and i<40:
            big=i
    return list1.index(big)

def crossover_(list):
    point_of_crossover=4
    for i in range(0,64,2):
        for j in range(point_of_crossover+1):
            if i+1<len(list):
                temp=list[i][j]
                list[i][j]=list[i+1][j]
                list[i+1][j]=temp
    return list

def mutation_(list):
    for i in range(64):
        for j in range(4,7):
            if list[i][j]==0:
                list[i][j]=1
            else:
                list[i][j]=0
    return list

def main_():
    list=random_()
    list1,list2=fitness_(list)
    index_of_big=selection_(list1)
    print("Best individual from random is",list[index_of_big],"with profit",list1[index_of_big],"and weight",list2[index_of_big])
    
    list=crossover_(list)
    list1,list2=fitness_(list)
    index_of_big=selection_(list1)
    print("Best individual after crossover is",list[index_of_big],"with profit",list1[index_of_big],"and weight",list2[index_of_big])
    
    list=mutation_(list)
    list1,list2=fitness_(list)
    index_of_big=selection_(list1)
    print("Best individual after mutation is",list[index_of_big],"with profit",list1[index_of_big],"and weight",list2[index_of_big]) 
    
if __name__ == '__main__':
    main_()