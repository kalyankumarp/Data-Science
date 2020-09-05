# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:30:20 2019

@author: kalya
"""

import pandas as pd
dat = [10,20,30]
labels = ["a", "b", "c"]
d = {"a":1, "b": 2, "c":3}
p = pd.Series(dat, labels)
print(p)
p = pd.Series(dat,d)
print(p)