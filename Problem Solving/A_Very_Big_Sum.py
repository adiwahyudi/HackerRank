#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

print(sum(ar))