# -*- coding: utf-8 -*-

import numpy as np

X = np.array([1,2]) # 1x2의 행렬
print(X.shape) #X.shape 이용해 '튜플'로 배열 모양 반환
print(X.ndim) #X.ndim 이용해 행렬의 차원 수 반환

W = np.array([[1, 3, 5],[2, 4, 6]])

Y = np.dot(X,W)  #np.dot(A,B) A,B의 내적 구해줌
print(Y)