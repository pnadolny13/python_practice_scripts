# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:19:36 2016

@author: pnadolny
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_list = []

for i in a:
	if i < num:
		new_list.append(i)

print (new_list)

