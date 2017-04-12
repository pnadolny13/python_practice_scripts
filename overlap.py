# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:00:24 2016

@author: pnadolny
"""
import random
a = random.sample(range(10), 8)
b = random.sample(range(10), 5)
c = []
for num in b:
    if num in a:
        c.append(num)
print (c)
    
    
    