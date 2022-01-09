# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 23:35:36 2022

@author: Doshite368
"""

import numpy as np
import matplotlib.pyplot as plt

#sin 함수 만들기
'''
x = np.arange(0, 6, 0.1) #return 하는 것이 array(행렬)인 range
y = np.sin(x)
# np.arange() 함수는 인자로 받는 값 만큼 1씩 증가하는 1차원 array를 만든다.
# 이때 하나의 인자만 입력하면 0 ~ 입력한 인자, 값 만큼의 크기를 가진다.
plt.plot(x, y)
plt.show()
'''

#sin cos 함수 만들기

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label='sin')
plt.plot(x,y2, linestyle='--', label="cos")
plt.xlabel("x축")
plt.ylabel("y축")
plt.title("사인,코사인")
plt.legend()
plt.show()



from matplotlib.image import imread

img = imread('pic.png')
plt.imshow(img)
plt.show()