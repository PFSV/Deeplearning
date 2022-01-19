# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:31:13 2022

@author: Doshite
"""
#ReLU function

def Relu(x):
    if x > 0:
        return x
    else:
        return 0
    
print(Relu(5), Relu(0), Relu(-7))
#5, 0, 0의 값이 나와야함 

print("numpy 이용")
import numpy as np

#np.maximum(a,b) : a,b 중 큰 값 반환함.

def Relu_n(x):
    return np.maximum(0,x)

print(Relu_n(5), Relu_n(0), Relu_n(-7))