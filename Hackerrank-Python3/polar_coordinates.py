# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
import math
s = complex(input())
d = math.sqrt((s.real * s.real) + (s.imag * s.imag))
print(d)
print(phase(complex(s.real, s.imag)))

# Constraints

# Given number is a valid complex number

# Output Format

# Output two lines:
# The first line should contain the value of r.
# The second line should contain the value of phi.

# Sample Input

#   1+2j
# Sample Output

#  2.23606797749979
#  1.1071487177940904
# Note: The output should be correct up to 3 decimal places.
