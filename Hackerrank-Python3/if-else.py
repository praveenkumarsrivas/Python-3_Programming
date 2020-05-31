# Task
# Given an integer, , perform the following conditional actions:

# If is odd, print Weird
# If is even and in the inclusive range of  to, print Not Weird
# If is even and in the inclusive range of  to, print Weird
# If is even and greater than, print Not Weird

n = int(input())
if (n % 2 != 0):
    print('weird')
elif (n % 2 == 0 and n >= 2 and n <= 5):
    print('Not Weird')
elif (n % 2 == 0 and n >= 6 and n <= 20):
    print('weird')
else:
    print("Not Weird")
