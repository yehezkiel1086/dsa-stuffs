#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    tt = 1
    for x in s:
        if x.isupper():
            tt += 1
    return tt

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)
    
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
