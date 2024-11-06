#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    arr = list(s)
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            del arr[i]
            del arr[i]
            i = 0
            continue
        i += 1
    if len(arr) == 0:
        return "Empty String"
    return "".join(arr)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)
    
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
