# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 01:22:55 2021

@author: subha
"""

def kangaroo(x1, v1, x2, v2):
        if (x1>x2 and v2<v1) or (x2>x1 and v2>v1) or (x1!=x2 and v1==v2):
            print("NO")
        elif(v1==v2 and x1==x2):
            print("YES")
        else:
            d_kangaroo1=x1
            d_kangaroo2=x2
            if d_kangaroo1-d_kangaroo2>0:
                while True:
                    d_kangaroo1=d_kangaroo1+v1
                    d_kangaroo2=d_kangaroo2+v2
                    if d_kangaroo1==d_kangaroo2:
                        print("YES")
                        break
                    if d_kangaroo1-d_kangaroo2<0:
                        print("NO")
                        break
            if d_kangaroo1-d_kangaroo2<0:
                while True:
                    d_kangaroo1=d_kangaroo1+v1
                    d_kangaroo2=d_kangaroo2+v2
                    if d_kangaroo1==d_kangaroo2:
                        print("YES")
                        break
                    if d_kangaroo1-d_kangaroo2>0:
                        print("NO")
                        break
        
        
        