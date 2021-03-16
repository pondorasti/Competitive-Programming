#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    total_count = 0
    string_length = len(s)

    # Fitt
    nr_fits = n // string_length
    appearances = 0
    for char in s:
        if char == "a":
            appearances += 1
    total_count += nr_fits * appearances

    # Remainder
    remainder = n - string_length * nr_fits
    for index in range(remainder):
        if s[index] == "a":
            total_count += 1

    return total_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
