# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:46:32 2021

@author: subha
"""

def timeConversion(s):
    list=[]
    list=s.split(":")
    if list[2][2]=="A" and int(list[0])==12:
        list[0]=int(list[0])-12
    
    if list[2][2]=="P" and int(list[0])!=12:
       list[0]=int(list[0])+12
       
    if len(str(list[0]))==2:
        print(str(list[0])+":"+list[1]+":"+list[2][0]+list[2][1])
    else:
        print("0"+str(list[0])+":"+list[1]+":"+list[2][0]+list[2][1])    