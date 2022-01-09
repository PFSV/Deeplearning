# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:32:43 2022

@author: Doshite368
"""

import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

#element wise , element num = equal

print("\n_element wise_")

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print("",x + y,"\n",x-y,"\n",x*y,"\n",x/y)

print("\n_element broadcast_")

x = np.array([1.0, 2.0, 3.0])
print(x/2)


print("\n_multiple array")

A = np.array([[1,2],[3,4]]) 
B = np.array([10,20])
print(A)
print(A*10)      #broadcast 1
print(A*B)       #broadcast 2 원소별 연산
print(A.shape)   #shape = 행렬의 형상
print(A.dtype)   #dtype = 행렬 안의 원소의 자료형



print("\n_numpyElementAccess_")

X = np.array([[51,55],[14,19],[0,4]])

print(X)
print(X[0]) #0번 index 전체 = 51,55
print(X[0][1]) #0번 인덱스에서 1번째 인덱스 = 55
