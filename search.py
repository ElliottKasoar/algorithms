#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:16:00 2020

@author: Elliott
"""

# Searching algorithm. Use either linear or binary (requires sorted list)

import numpy as np
import time

# =============================================================================
# Linear search algorithm
# =============================================================================

# Loops through all elements in array and compares to target value
def linear_search(arr, search_val):
    
    length = len(arr)
    
    for i in range(length):
        if (arr[i] ==  search_val):
            return i
    
    return -1
  
# =============================================================================
# Binary search algorithm(s)
# =============================================================================

# Takes in array to be searched through, search value and index being tracked
# Recursively divides array by comparing middle value to target
# Returns index if found, or -1 if not
def binary_search_rec_split(arr, search_val, index):
    
    length = len(arr)
    
    if (length > 1):
        
        mid = length//2
        
        if (search_val >= arr[mid]):
            index += mid
            index = binary_search_rec_split(arr[mid:], search_val, index) 
        else:
            index = binary_search_rec_split(arr[:mid], search_val, index)
    
    elif (arr[0] != search_val):
        return -1
    
    return index


# Takes in array to be searched, search value and left and right indices
# Recursively searches array by comparing target to mid point between left 
# and right indicies. Left or right index changed if value greater or smaller
# Returns index if found, or -1 if not.
def binary_search_rec_lr(arr, search_val, l, r):
        
    if (l <= r):
        
        mid = (l+r)//2 
        # print("Mid: ", mid)
        
        if (arr[mid] == search_val):
            return mid
    
        elif (search_val > arr[mid]):
            return binary_search_rec_lr(arr, search_val, (mid + 1), r)
        else:
            return binary_search_rec_lr(arr, search_val, l, (mid - 1))
   
    else:
        return -1


# Takes in array to be searched through and search value
# Searches array in loop by comparing target to mid point between left 
# and right indicies. Left or right index changed if value greater or smaller
# Returns index if found, or -1 if not.
def binary_search_loop(arr, search_val):
        
    length = len(arr)
    l = 0
    r = length - 1
    
    while (l <= r):
        
        mid = (l+r)//2
        
        if (arr[mid] == search_val):
            return mid
        elif (search_val > arr[mid]):
            l = mid + 1
        else:
            r = mid -1
        
    return -1

# =============================================================================
# Main
# =============================================================================

def main(linear_flag, search_val):
    
    values = np.linspace(1,10,10) #Ordered list (can be randomised)

    if (linear_flag):
        np.random.shuffle(values) #Shuffle to create unodered list
    
    print("Searching for: ", search_val)
    # print("List: ", values)
        
    #Run main code - linear or binary
    if (linear_flag):
        t1= time.time()
        index = linear_search(values, search_val)
        t2= time.time()
        dt = t2 - t1
    elif (loop_flag):
        t1= time.time()
        index = binary_search_loop(values, search_val)
        t2= time.time()
        dt = t2 - t1   
    elif (split_flag):
        t1= time.time()
        index = 0
        index = binary_search_rec_split(values, search_val, index)
        t2= time.time()
        dt = t2 - t1
    else:
        t1= time.time()
        l = 0
        r = len(values) - 1
        index = binary_search_rec_lr(values, search_val, l, r)
        t2= time.time()
        dt = t2 - t1    

    if (index > -1):
        print("Value found. Index = ", index)
    else:
        print("Value not found.")
 
    print("Time taken = ", dt)

# =============================================================================
# Run code
# =============================================================================

# Binary search orders of mag quicker but must be ordered 
# (Will shuffle for demonstration)
# For binart search, loop or recursive with l and r indices much quicker
# Do not have to create mutltiple new arrays as with dividing the array (split)

linear_flag = False #Use linear search algorithm (or binary)
loop_flag = True #Use loop with left and right indicies updated as necessary
split_flag = False #Uses recursive search to split array repeatedly
#If all false will recursively search, updating left and right indices

search_val = 3 #Value searching for
main(linear_flag, search_val)
