#!/bin/python3

import sys

"""
Link: https://www.hackerrank.com/challenges/almost-sorted/problem
"""

def checkSorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def almostSorted(arr):
    if len(arr) == 1 or checkSorted(arr):
        print("yes")
        return

    # Find first item out of order from the left
    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i+1]:
        i+=1
    first_ooo_left = i

    # Find first item out of order from the right
    i = len(arr) - 1
    while i > 0 and arr[i-1] < arr[i]:
        i-=1
    first_ooo_right = i

    # Same item?
    if (first_ooo_left == first_ooo_right):
        print("no")
        return

    l = first_ooo_left
    r = first_ooo_right
    swaps = 0
    while r-l > 0:
        if arr[l] > arr[r]: 
            arr[r], arr[l] = arr[l], arr[r]
            swaps += 1
        r-=1
        l+=1

    sorted = checkSorted(arr)

    if sorted:
        if swaps == 1:
            print("yes")
            print("swap " + str(first_ooo_left+1) + " " + str(first_ooo_right+1))
        elif swaps == (first_ooo_right-first_ooo_left+1)//2:
            print("yes")
            print("reverse " + str(first_ooo_left+1) + " " + str(first_ooo_right+1))
    else:
        print("no")

