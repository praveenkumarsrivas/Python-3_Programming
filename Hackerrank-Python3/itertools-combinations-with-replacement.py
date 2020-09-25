# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
string, n = input().split()
lst = list()
lst = list(string)
lst.sort()
#print(lst)
string = "".join(lst)
n = int(n)
l = list((combinations_with_replacement(string, n)))
# print(l)
l.sort()
for x in l:
    print("".join(x))
