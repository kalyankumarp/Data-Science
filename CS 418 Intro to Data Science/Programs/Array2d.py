# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:53:40 2019

@author: kalya
"""
import numpy as np
arr_2d = np.arange(50).reshape(5,10)
arr = arr_2d[2:5, 1:5]
print(arr)
print(arr[arr>30])
print(np.ones(10)*4)
print(np.random.rand(5))
print(np.random.randn(4,4))
print(np.random.randint(9))
print((np.arange(1,101)*0.01).reshape(10,10))