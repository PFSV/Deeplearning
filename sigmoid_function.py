# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:21:00 2022

@author: Doshite
"""

import numpy as np #수학 관련은 numpy
import matplotlib.pyplot as plt #그래프 구현은 pyplot #matplotlib.pyplot이라 적어야함

def sigmoid(x):
    return 1/ (1+np.exp(-x)) #시그모이드 함수 정의  1/ (1+exp(x))

x = np.arange(-5.0, 5.0, 0.1) #np.arange(a,b,c) a= 시작, b = 끝, c= 간격, 배열 생성, []이용해 2차원 이상 가능

y = sigmoid(x) # 함수 설정

plt.plot(x,y) #plot(x,y) =  x,y에 대해 그래프 표현
plt.ylim(-0.1, 1.1) #ylim(a,b) a= 하한선, b = 상한선, y의 기준 설정
plt.show()

# 왜 sigmoid 함수를 neural network 에 사용하는가?