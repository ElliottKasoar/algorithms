#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:48:06 2020

@author: Elliott
"""

# Bubble sort algorithm

import numpy as np
import time

# Bubble sort function.
# Compares adjacent pairs of elements and swaps if first element is larger
# Repeats this (length of array - 1) times, each time one fewer element must be
# considered.
def bubble_sort(arr):
    
    length = len(arr)
    
    for i in range(length - 1):
        for j in range(length - i - 1):    
            
            if (arr[j] > arr[j+1]):        
            
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

        # print(arr)

# Main
def main():
    
    ol = np.linspace(1,1000,1000) #Ordered list to compare with at end.
    ul = ol.copy() #Copy else just renames ol as ul and will still be shuffled
    np.random.shuffle(ul) #Shuffle to create unodered list
    
    # print("ol: ", ol)
    # print("ul: ", ul)
        
    #Run main code
    
    t1= time.time()
    bubble_sort(ul)
    t2= time.time()
    dt = t2 - t1

    # print("Final list: ", ul)

    if (np.array_equal(ol, ul)):
        print("Sorted!")
        print("Time taken = ", dt)
    else:
        print("Not sorted.")

#Run code
main()