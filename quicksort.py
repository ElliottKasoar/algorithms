#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:01:09 2020

@author: Elliott
"""

# Quicksort algorithm

import numpy as np
import time

def quicksort(arr):
    
    length = len(arr)
    
    if (length > 1):
        pivot = arr[length - 1]
        partition = 0
        
        for i in range(length):
        
            if (arr[i] < pivot):
                
                if (i <= partition):
                    partition += 1
                else:
                    temp = arr[partition]
                    arr[partition] = arr[i]
                    arr[i] = temp
                    partition += 1
            
            if (arr[i] == pivot):
                temp = arr[partition]
                arr[partition] = arr[i]
                arr[i] = temp
                    
        # print("ul: ", arr)
        
        quicksort(arr[:partition])
        quicksort(arr[(partition + 1):])

def main():
    
    ol = np.linspace(1,10,10) #Ordered list to compare with at end.
    ul = ol.copy() #Copy else just renames ol as ul and will still be shuffled
    np.random.shuffle(ul) #Shuffle to create unodered list
    
    print("ol: ", ol)
    print("ul: ", ul)
        
    #Run main code
    
    t1= time.time()
    quicksort(ul)
    t2= time.time()
    dt = t2 - t1

    print("Final list: ", ul)

    if (np.array_equal(ol, ul)):
        print("Sorted!")
        print("Time taken = ", dt)
    else:
        print("Not sorted.")

main()