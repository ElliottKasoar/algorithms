#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:55:44 2020

@author: Elliott
"""

# Sorting algorithm. Not quite merge sort (?) since not always divided equally
# Current implementation sorts into pairs, then fours, then eights etc
# Remainder that doesn't divide into power of two also sorted
# Means final merge not necessarily close to even e.g. could be 16 and 2

# E.g. list of 20
# 20x 1s -> 10x 2s -> 5x 4s -> 2x 8s and a 4 -> 1x 16 and a 4 -> 20

import numpy as np
import math
import time

# =============================================================================
# Merge arrays
# =============================================================================

# Function to merge two ordered arrays, a and b, into new ordered array, c.
# Initial arrays often same length but will not always be unless...
# ...final array is power of 2. Inputs a and b, returns c.
def mergeFunc(a, b):
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
# Main
# =============================================================================

# Loop sort
def loop_sort(ul):
    
    length = len(ul) #Could use np.size or np.shape[0]

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
            
        #Merge pairs
        for j in range(arr_num):
            
            x = j * pair_arr_size
            ul[x:x + pair_arr_size] = mergeFunc(ul[x:x + init_arr_size], ul[x + init_arr_size:x + 2 * init_arr_size])
        
        #Need to merge any residual elements if greater than previous merge size
        residual = np.mod(length, pair_arr_size)
                
        # mergeFunc needs ordered lists to be merged
        #If combining one at end won't necessarily be in order if split in half
        #But previous pair size will be ordered, and remainder will also be ordered
        
        if (residual > init_arr_size):
            # print("test!")
            ul[-residual:] = mergeFunc(ul[-residual:-(residual-init_arr_size)], ul[-(residual-init_arr_size):])
        
        # print("ul: ", ul)


# =============================================================================
# Reecursive sort
# =============================================================================

def recursive_sort(full_arr):
    
    length = len(full_arr)
    
    # half_length = length//2
    # left_arr = full_arr[:half_length]
    # right_arr = full_arr[half_length:]
    
    # print("left array before merge: ", left_arr)
    # print("right array before merge: ", right_arr)
    # print("full array before merge: ", full_arr)
    # full_arr[:] = mergeFunc(left_arr, right_arr)
    # print("left array after merge: ", left_arr)
    # print("right array after merge: ", right_arr)
    # print("full array after merge: ", full_arr)
    
    # full_arr[0] = 100
    
    if (length > 1):
        
        half_length = length//2
        left_arr = full_arr[:half_length]
        right_arr = full_arr[half_length:]
        
        recursive_sort(left_arr)
        recursive_sort(right_arr)    
        
        print("left array: ", left_arr)
        print("right array: ", left_arr)
        print("full array: ", full_arr)
        full_arr[:] = mergeFunc(left_arr, right_arr)
        print("left array: ", left_arr)
        print("right array: ", left_arr)
        print("full array: ", full_arr)


# =============================================================================
# Useful values
# =============================================================================

# Will be ordered lowest to highest

ol = np.linspace(1,20,20) #Ordered list to compare with at end.
ul = ol.copy() #Copy else just renames ol as ul and will still be shuffled
np.random.shuffle(ul) #Shuffle to create unodered list
print("ol: ", ol)
print("ul: ", ul)

# ul= np.array([3, 4, 1, 2])
# ul = [3, 4, 1, 2]

#Run main code
t1= time.time()
recursive_sort(ul)
t2= time.time()
dt = t2 - t1

print("Final list: ", ul)

# print("'Unordered' list: ", ul)
if (np.max(np.subtract(ul, ol)) == 0):
    print("Sorted!")
    print("Time taken = ", dt)
else:
    print("Not sorted.")

