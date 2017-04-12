# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:38:06 2017

@author: pnadolny
"""
#####As what they want###
var = input ("What would you like to buy today?" )
print ("Ok, you will be having 1 " + var)


shopping_list = [var]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] = stock[item] - 1
    print ("That will cost you: ") 
    print (total)
### calculate price and new stock###
food = ["banana", "orange", "apple", "orange","orange"];
compute_bill(shopping_list)
print (stock)

