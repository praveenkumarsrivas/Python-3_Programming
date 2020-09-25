# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import itertools


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


n = int(input())
l = input().split()
k = int(input())
matchlst = list()
for x in range(len(l)):
    if l[x] == 'a':
        matchlst.append(x + 1)
c = 0
newlst = (list(itertools.combinations(l, k)))
for x in newlst:
    if 'a' in x:
        c += 1
print(c / nCr(n, k))
