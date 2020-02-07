#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:06:33 2020

@author: warre112
"""

"""
Asignment 01- ABE 651
Les Warren
Created Monday, January 20, 2020

This  program creates functions to print a variable twice and how to give a 
function multiple arguments

"""
def do_twice(f):
    f()
    f()
#operates function twice
def print_spam():
    print('spam')

## ':' allows to specify on next line(s)

def do_twice(f, val):   
    f(val)
    f(val)

## f= function
## val= value (argument of the function)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')
