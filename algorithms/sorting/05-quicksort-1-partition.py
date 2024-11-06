#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def partition(arr, l, h):
    i = l - 1
    pvt = arr[h]
    
    for j in range(l, h):
        if arr[j] <= pvt:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i + 1

def quickSort(arr, l, h):
    # Write your code here
    if l < h:
        pi = partition(arr, l, h)
        
        # left
        quickSort(arr, pi + 1, h)
        
        # right
        quickSort(arr, l, pi - 1)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    quickSort(arr, 0, len(arr) - 1)
    
    result = arr
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
