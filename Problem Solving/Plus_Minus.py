#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    i,pos,neg,zero = 0,0,0,0
    while i < (len(arr)):
        if arr[i] > 0:
            pos = pos + 1
        elif arr[i] < 0:
            neg = neg + 1
        elif arr[i] == 0:
            zero = zero + 1
        i = i + 1
    print(format(pos/n,'.6f'))
    print(format(neg/n,'.6f'))
    print(format(zero/n,'.6f'))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
