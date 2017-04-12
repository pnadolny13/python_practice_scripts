# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:14:15 2016

@author: pnadolny
"""
number = input("Choose a number: ")
number = int(number)

x = range(2,number)
print ("The divisors of " + str(number) + " are: ")
for elem in x:
    remainder = number % int(elem)
    if remainder == 0 :
        print (elem)
        
