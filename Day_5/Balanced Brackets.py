#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    openers = ['(', '{', '[']
    closers = {
        ')': '(', 
        '}': '{', 
        ']': '['
    }
    bracket_stack = []
    for c in s:
        if c in openers:
            bracket_stack.append(c)
        elif c in closers:
            if len(bracket_stack) == 0:
                return 'NO'

            if bracket_stack.pop() != closers[c]:
                return 'NO'

    if len(bracket_stack) > 0:
        return 'NO'

    return 'YES'
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
