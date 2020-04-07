#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:55:44 2020

@author: Elliott
"""

import numpy as np

ol = np.linspace(0,9,10)
np.random.shuffle(ol)

# Assume even number of elements in list for now...
# Count length, not sure if will need but useful to know in general...
#Should be half length number of pairs
length = len(ol) #Could use np.size or np.shape[0]

for i in range(length//2):
    print(i)

print("test")
print("test 2")

