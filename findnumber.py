# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:20:34 2021

@author: subha
"""

def findNumber(arr, k):
    front=0
    back=len(arr)-1
    flag=0
    while front<=back:
        if (arr[front]==k) or (arr[back]==k):
            print("YES")
            flag=1
            break
        front=front+1
        back=back-1
    if flag==0:
        print("NO")