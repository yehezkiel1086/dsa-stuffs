#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    tt_l = 0
    tt_r = 0
    for i in range(n):
        tt_l += arr[i][i]
        tt_r += arr[i][n - i - 1]
    return abs(tt_l - tt_r)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
