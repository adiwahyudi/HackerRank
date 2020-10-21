#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maksAwal,minAwal = scores[0],scores[0]
    maks,min=0,0
    i = 1
    while i < len(scores):
        if scores[i]>maksAwal:
            maksAwal = scores[i]
            maks = maks + 1
        i = i + 1
    print("Banyak naik  : ",maks)
    i = 1
    while i < len(scores):
        if scores[i]<minAwal:
            minAwal = scores[i]
            min = min + 1
        i = i+1
    return maks,min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
