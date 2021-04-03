# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.
# Note: This challenge introduces precision problems.
# The test cases are scaled to six decimal places,
# though answers with absolute error of up to 10 ^6  are acceptable.



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive =0
    negitive =0
    zero =0
    
    for i in range(len(arr)):
        if arr[i]== 0:
            zero+=1
        elif arr[i] > 0 :
            positive +=1
        else:
            negitive +=1
    
    print(positive/(len(arr)))
    print(negitive/(len(arr)))
    print(zero/(len(arr)))
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
