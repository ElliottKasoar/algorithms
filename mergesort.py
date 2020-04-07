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

for i in range(length//2):
    # print(i)
    i

# Will be ordered lowest to highest

#First set of pairs:
if (ul[0] < ul[1]):
    pair_1 = np.array([ul[0], ul[1]])
else:
    pair_1 = np.array([ul[1], ul[0]])

if (ul[2] < ul[3]):
    pair_2 = np.array([ul[2], ul[3]])
else:
    pair_2 = np.array([ul[3], ul[2]])
    
if (ul[4] < ul[5]):
    pair_3 = np.array([ul[4], ul[5]])
else:
    pair_3 = np.array([ul[5], ul[4]])
    
if (ul[6] < ul[7]):
    pair_4 = np.array([ul[6], ul[7]])
else:
    pair_4 = np.array([ul[7], ul[6]])

if (ul[8] < ul[9]):
    pair_5 = np.array([ul[8], ul[9]])
else:
    pair_5 = np.array([ul[9], ul[8]])

print(pair_1)
print(pair_2)
print(pair_3)
print(pair_4)
print(pair_5)

# Second set of pairs: