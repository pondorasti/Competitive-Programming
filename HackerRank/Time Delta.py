#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    a1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    a2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    return abs(int(a1.timestamp() - a2.timestamp()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = str(time_delta(t1, t2))

        fptr.write(delta + '\n')

    fptr.close()
