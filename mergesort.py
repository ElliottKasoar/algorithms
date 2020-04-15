#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:55:44 2020

@author: Elliott
"""

# Merge sort algorithm. Implemented in two different ways:

# loop_sort function not quite merge sort (?) since not always divided equally
# Current implementation sorts into pairs, then fours, then eights etc
# Remainder that doesn't divide into power of two also sorted
# Means final merge not necessarily close to even e.g. could be 16 and 2
# E.g. list of 20
# 20x 1s -> 10x 2s -> 5x 4s -> 2x 8s and a 4 -> 1x 16 and a 4 -> 20

# recursive_sort function more usual implementation. Recursively divides list
# in two, then merges back together in order
# E.g. list of 20
# 20 <-> 2x 10s <-> 4x 5s <-> 4x 3s and 4x 2s <-> 8x 2s and 4x 1s <-> 20x 1s


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
# Sort using loop from bottom up
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
            ul[x:x + pair_arr_size] = mergeFunc(ul[x:x + init_arr_size], 
                                                ul[x + init_arr_size:x + 
                                                   2 * init_arr_size])
        
        # Merge any residual elements if greater than previous merge size
        residual = np.mod(length, pair_arr_size)
                
        # mergeFunc needs ordered lists to be merged
        # If combining one at end won't necessarily be ordered if split in half
        # But previous pair size will be ordered, 
        # and remainder will also be ordered
        
        if (residual > init_arr_size):
            # print("test!")
            ul[-residual:] = mergeFunc(ul[-residual:-(residual-init_arr_size)],
                                       ul[-(residual-init_arr_size):])


# =============================================================================
# Reecursive sort
# =============================================================================

#Use recursion to divide list in half repeatedly then merge together in order
def recursive_sort(full_arr):
    
    length = len(full_arr)
    
    if (length > 1):
        
        #Divide list in two
        half_length = length//2
        left_arr = full_arr[:half_length]
        right_arr = full_arr[half_length:]
        
        #Split each half further
        recursive_sort(left_arr)
        recursive_sort(right_arr)    
        
        #Merge two halves
        full_arr[:] = mergeFunc(left_arr, right_arr)


# =============================================================================
# Main
# =============================================================================

def main(recursive_flag):
    
    ol = np.linspace(1,10,10) #Ordered list to compare with at end.
    ul = ol.copy() #Copy else just renames ol as ul and will still be shuffled
    np.random.shuffle(ul) #Shuffle to create unodered list
    
    # print("ol: ", ol)
    # print("ul: ", ul)
        
    #Run main code. Either recursive function (divide and merge)
    # or via loop merging pairs etc from start
    
    if (recursive_flag):
        t1= time.time()
        recursive_sort(ul)
        t2= time.time()
        dt = t2 - t1
    else:
        t1= time.time()
        loop_sort(ul)
        t2= time.time()
        dt = t2 - t1
        
    # print("Final list: ", ul)

    if (np.array_equal(ol, ul)):
        print("Sorted!")
        print("Time taken = ", dt)
    else:
        print("Not sorted.")


# =============================================================================
# Run code
# =============================================================================

# Sort a list (or numpy array) from lowest to highest using merge sort

#Flag to decide whether to use recursion or not
recursive_flag = True
main(recursive_flag)

