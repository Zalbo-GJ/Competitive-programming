#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
  
    dp = {}
    dp[n] = quickMath(n)
    
    return int(quickMath(dp[n] * k))
    
    
    
    
def quickMath(n):
    
    if int(n) < 10:
        return n
    summ = 0   
    for i in n:
        summ += int(i)
    return quickMath(str(summ))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
