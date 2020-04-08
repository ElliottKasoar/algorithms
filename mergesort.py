#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:55:44 2020

@author: Elliott
"""

import numpy as np
import math

#Currently works for powers of two only

# =============================================================================
# Merge arrays
# =============================================================================

# Function to merge two ordered arrays, a and b, into new ordered array, c.
# Initial arrays often same length but will not always be unless...
# ...final array is power of 2. Inputs a and b, returns c.
def merge_func(a, b):
    length_a = len(a)
    length_b = len(b)
    length_c = length_a + length_b
    
    c = np.zeros(length_c)
    
    index_a = 0
    index_b = 0
    
    for i in range(length_c):
        
        if (index_a == length_a):
            c[i:] = b[index_b:]
            break
        
        if (index_b == length_b):
            c[i:] = a[index_a:]
            break
        
        if (a[index_a] < b[index_b]):
            c[i] = a[index_a]
            index_a += 1
        else:
            c[i] = b[index_b]
            index_b += 1

    return c

# =============================================================================
# Useful values
# =============================================================================


ol = np.linspace(0,15,16) #Ordered list to compare with at end.
ul = ol.copy() #Copy else just renames ol as ul and will still be shuffled
np.random.shuffle(ul) #Shuffle to create unodered list
print("ol: ", ol)
print("ul: ", ul)

# Length of (ordered list). Should be half length number of pairs
# Will be ordered lowest to highest
length = len(ol) #Could use np.size or np.shape[0]

# =============================================================================
# Main
# =============================================================================

#Say you have 20, then will have 
# 20x 1s -> 10x 2s -> 5x 4s -> 2x 8s and a 4 -> 1x 16 and a 4 -> 20
#Largest array given by 2^4. Can access this number using log
# Number of merges given by this number + 1 (since not a power of 2)

power_num = int(math.log2(length))
remainder = length - pow(2, power_num)

if (remainder != 0):
    merge_num = power_num + 1
else:
    merge_num = power_num

for i in range(merge_num):
    
    init_arr_size = pow(2, i)
    pair_arr_size = 2 * init_arr_size
    
    arr_num = length // pair_arr_size
    
    # print("Pair size: ", pair_arr_size)
    
    for j in range(arr_num):
        
        x = j * pair_arr_size
        # print("x: ", x)
        ul[x:x + pair_arr_size] = merge_func(ul[x:x + init_arr_size], ul[x + init_arr_size:x + 2 * init_arr_size])
    
    # print(ul)

print("Unordered list: ", ul)
if (np.min(np.subtract(ul, ol)) == 0):
    print("Sorted!")



