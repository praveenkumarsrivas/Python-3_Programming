# Output Format

# First, print the mean.
# Second, print the var.
# Third, print the std.

# Sample Input

# 2 2
# 1 2
# 3 4
# Sample Output

# [1.5  3.5]
# [1.  1.]
# 1.11803398875

import numpy
n, m = input().split()
n = int(n)
m = int(m)
l = list()
arr = list()
arr = []
x = 0
i = 0
for x in range(n):
    l = input()
    l = [int(y) for y in l.split(" ")]
    arr.append(l)
#print(arr)
numpy.set_printoptions(legacy='1.13')
# np.arr().astype(np.int)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr, axis=None))


#read about the function set_printoptions