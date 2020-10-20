#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

print(sum(ar))