# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:41:06 2020

@author: krish
"""

def checkNum(num):
    iterations=1
    
    while(num!=1):
        if(num%2==0):
            num=int(num/2)
            iterations+=1
        else:
            num=(num*3)+1
            iterations+=1
            
    print(num,iterations)
    
checkNum(20)
            