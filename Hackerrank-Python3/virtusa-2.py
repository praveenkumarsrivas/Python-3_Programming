import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):
    d = 0
    for i in range(len(s)):
        if i + 1 != len(s) and s[i] == s[i + 1]:
            d += 1
    return d


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)
