# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:43:24 2020

@author: sankalp
"""

def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """
    n = len(ints)
    smallest = 9999999
    largest = -1
    if n<1:
        return 
    
    for i in ints:
        if i<smallest:
            smallest = i
        if i>largest:
            largest = i  
    return (smallest, largest)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max_by_sorting([0])) else "Fail")
print ("Pass" if (None == get_min_max_by_sorting([])) else "Fail")