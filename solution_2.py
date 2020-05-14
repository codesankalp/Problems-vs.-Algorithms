# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:43:40 2020

@author: sankalp
"""
def get_pivot(input_list,number):
    l = len(input_list)
    if l==0:
        return 
    low = 0
    high = l
    while low <= high:
        pivot = (low+high) // 2
        if input_list[pivot-1] > input_list[pivot]:
            break
        elif input_list[0] < input_list[pivot]:
            low = pivot
        elif input_list[0] > input_list[pivot]:
            high = pivot 
    return pivot

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    l = len(input_list)
    pivot = get_pivot(input_list, number)
    if pivot is None:
        return -1
    if input_list[pivot] <= number and input_list[l-1] >= number:
        low = pivot
        high = l
    else:
        low = 0
        high = pivot

    while low <= high:
        pivot = (low+high) // 2
        if input_list[pivot] == number:
            return pivot
        elif input_list[pivot] < number:
            low = pivot+1
        else:
            high = pivot-1
    return -1   

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#edge cases
test_function([[2,1], 0])  #element not present
test_function([[], 0])  #list is empty