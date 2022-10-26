# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:05:04 2021

@author: subha
"""

def birthday(s, d, m):
    n=0
    sum=0
    count=0
    while True:
        for i in range(n,m):
            sum+=s[i]
            if sum==d:
                count+=1
        n+=1
        m+=1
        sum=0
        if m>=len(s):
            break
    return(count)