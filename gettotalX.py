# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:20:22 2021

@author: subha
"""

def getTotalX(a, b):
    count=0
    count1=0
    final_count=0
    list=[]
    for element in range(max(a),min(b)+1):
        for n1 in a:
            if element%n1==0:
                count+=1
                
        if count==len(a):
            for n2 in b:
                if n2%element==0:
                    count1+=1
        
        if count1==len(b):
            final_count+=1
            list.append(element)
        count=0
        count1=0
    return(final_count)
                