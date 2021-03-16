#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):

    current_level = 0
    valley_count = 0
    isInValley = False

    for step in path:
        # Check for Valley State
        if step is "D" and current_level is 0:
            isInValley = True
        elif step is "U" and current_level is -1 and isInValley is True:
            isInValley = False
            valley_count += 1

        # Update current_level
        if step is "D":
            current_level -= 1
        else:
            current_level += 1

    return valley_count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
