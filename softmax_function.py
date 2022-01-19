# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:33:18 2022

@author: Doshite
"""

import numpy as np

def softmax(x):
    c = np.max(x)
    expx = np.exp(x-c)
    summ_expx = np.sum(expx)
    y = expx / summ_expx
    return y

