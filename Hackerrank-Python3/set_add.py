# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = set()
for i in range(n):
    x = input()
    lst.add(x)
print(len(lst))
