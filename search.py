#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:16:00 2020

@author: Elliott
"""

# Searching algorithm. Use either linear or binary (requires sorted list)

import numpy as np
import time

def linear_search(arr, search_val):
    
    length = len(arr)
    
    for i in range(length):
        if (arr[i] ==  search_val):
            return i
    
    return -1
    
def binary_search(arr, search_val, index):
    
    length = len(arr)
    
    if (length > 1):
        
        mid = length//2
        
        if (search_val >= arr[mid]):
            index += mid
            index = binary_search(arr[mid:], search_val, index) 
        else:
            index = binary_search(arr[:mid], search_val, index)
    
    elif (arr[0] != search_val):
        return -1
    
    return index

def main(linear_flag, search_val):
    
    values = np.linspace(1,10,10) #Ordered list (can be randomised)
    
    if (linear_flag):
        np.random.shuffle(values) #Shuffle to create unodered list
    
    print("Searching for: ", search_val)
    print("List: ", values)
        
    #Run main code
    
    if (linear_flag):
        t1= time.time()
        index = linear_search(values, search_val)
        t2= time.time()
        dt = t2 - t1
    else:
        t1= time.time()
        index = 0
        index = binary_search(values, search_val, index)
        t2= time.time()
        dt = t2 - t1        

    if (index > -1):
        print("Value found. Index = ", index)
    else:
        print("Value not found.")
 
    print("Time taken = ", dt)

linear_flag = False
search_val = 11
main(linear_flag, search_val)
