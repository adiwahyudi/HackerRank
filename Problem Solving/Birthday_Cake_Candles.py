#!/bin/python3

import math
import os
import random
import re
import sys

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))

print(candles.count(max(candles)))  
