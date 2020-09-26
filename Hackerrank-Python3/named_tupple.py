# Collections.namedtuple()

from collections import namedtuple
n = int(input())
fields = input().split()
total = 0
Details = namedtuple('Details', fields)
for i in range(n):
    f1, f2, f3, f4 = input().split()
    student = Details(f1, f2, f3, f4)
    total += int(student.MARKS)
print(total / n)

##### INPUT ####
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
#
# ### OUTPUT ###
# 78.00
