# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:47:44 2020

@author: sankalp
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number ** 2 == number:
        return number
    start = 0
    end = number
    while start <= end:
        mid = (start + end) // 2
        if (mid**2 == number):
            return mid
        elif (mid**2 <= number and (mid+1)**2 > number):
            return mid
        elif (mid**2 > number):
            end = mid
        else:
            start = mid

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")