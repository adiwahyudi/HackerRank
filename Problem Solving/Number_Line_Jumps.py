#!/bin/python3

import math

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a = (x1-x2)
    b = (v2-v1)
    
    if b == 0:
        formula = a
    else:
        formula = (x1-x2)/(v2-v1)

    if (formula == math.floor(formula) and formula > -1):
        return "YES"
    else:
        return "NO"    

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
