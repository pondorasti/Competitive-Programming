#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.s
def jumpingOnClouds(c):
    numberOfJumps = 0
    currentIndex = 0

    while currentIndex + 1 < len(c):
        if currentIndex + 2 < len(c) and c[currentIndex + 2] == 0:
            numberOfJumps += 1
            currentIndex += 2
        else:
            numberOfJumps += 1
            currentIndex += 1

    return numberOfJumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
