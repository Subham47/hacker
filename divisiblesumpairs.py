# -*- coding: utf-8 -*-
"""
Created on Wed May 26 16:34:49 2021

@author: subha
"""

def divisibleSumPairs(n, k, ar):
    sum=0
    count=0
    for i in range(n-1):
        j=i+1
        while(j<n):
            sum=ar[i]+ar[j]
            if sum%k==0:
                print(ar[i],ar[j])
                count+=1
            j+=1
            sum=0
    return count     
            
        
        