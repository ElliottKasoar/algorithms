#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:55:44 2020

@author: Elliott
"""

import numpy as np

ol = np.linspace(0,9,10)
ul = ol.copy() #Otherwise just renames ol as ul and will still be shuffled
np.random.shuffle(ul)
print("ol: ", ol)
print("ul: ", ul)

# Assume even number of elements in list for now...
# Count length, not sure if will need but useful to know in general...
#Should be half length number of pairs
length = len(ol) #Could use np.size or np.shape[0]


# Will be ordered lowest to highest

# =============================================================================
# First set of pairs:
# =============================================================================

for i in range(length//2):
    
    x = 2*i
    temp = ul[x+1]
    
    if (ul[x] > ul[x+1]):
        ul[x+1] = ul[x]
        ul[x] = temp

print("Pairs ordered: ", ul)

# =============================================================================
# Second set of pairs:
# =============================================================================
 
for i in range(length//4):

    x = 4*i
    temp1 = ul[x+2]
    temp2 = ul[x+3]

    if (ul[x+1] > ul[x+2]):
        if (ul[x+1] > ul[x+3]):
            
            if (ul[x] > ul[x+2]):
                if (ul[x] > ul[x+3]):
                    ul[x+3] = ul[x+1]
                    ul[x+2] = ul[x]
                    ul[x+1] = temp2
                    ul[x] = temp1
                else:
                    ul[x+3] = ul[x+1]
                    ul[x+2] = temp2
                    ul[x+1] = ul[x]
                    ul[x] = temp1
            else:
                ul[x+3] = ul[x+1]
                ul[x+2] = temp2
                ul[x+1] = temp1
        else:
            if (ul[x] > ul[x+2]):
                ul[x+2] = ul[x+1]
                ul[x+1] = ul[x]
                ul[x] = temp1
            else:
                ul[x+2] = ul[x+1]
                ul[x+1] = temp1

print("Fours ordered(?): ", ul)
  
# =============================================================================
# Third set of pairs        
# =============================================================================

for i in range(length//8):
    x = 8*i
    
