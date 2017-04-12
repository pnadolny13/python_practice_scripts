# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:27:30 2016

@author: pnadolny
"""

def fizz_count(x):
    count = 0
    for item in x:
        if item =="fizz":
            count = count + 1
    print (count)
a = ["fizz","cat","dog"]
print (fizz_count(a))