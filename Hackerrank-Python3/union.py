n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))
res = (set(a).union(set(b)))
print(len(res))