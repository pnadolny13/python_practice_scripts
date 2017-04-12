# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:33:13 2016

@author: pnadolny
"""

number = int(input("Choose any number: "))
remain = number%2
remain2 = number%4
if remain != 0 :
    print ("your number is odd")
elif remain2 == 0:
    print("your number is divisible by 4")
else :
    print ("your number is even")