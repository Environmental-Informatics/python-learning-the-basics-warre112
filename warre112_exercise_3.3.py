#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:54:42 2020

@author: warre112
"""
"""
Assingment 01
Les Warren
Created Monday, January 20, 2020

This program creates a function to print a 4x4 grid. Uses functions that print 
can print variable multiple times


"""
hortizontal = "+ - - - - + - - - - + - - - - + - - - - +"
#variable for boarder

vertical = "|         |         |         |         |"
#variable for grid height


def printfour(x):
    print(x)
    print(x)
    print(x)
    print(x)
#prints variable "x" four times
def print_grid():
    print (hortizontal) #prints hortizontal
    printfour(vertical) #prints printfour function (prints vertical 4 times)
    print (hortizontal)
    printfour (vertical)
    print (hortizontal)
    printfour (vertical)
    print (hortizontal)
    printfour (vertical)
    print (hortizontal)
#creates a function to print 4x4 grid using the print function and the printfour function created above 

print_grid() #tests function
