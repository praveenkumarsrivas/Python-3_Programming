# Output Format

# Print the matrix multiplication of A and B .

# Sample Input

# 2
# 1 2
# 3 4
# 1 2
# 3 4
# Sample Output

# [[7 10]
#  [15 22]]

import numpy
n = int(input())
a = []
b = []
l = list()
for x in range(n):
    l = input()
    l = [int(i) for i in l.split(" ")]
    a.append(l)

for x in range(n):
    l = input()
    l = [int(i) for i in l.split(" ")]
    b.append(l)

print(numpy.dot(a, b))

