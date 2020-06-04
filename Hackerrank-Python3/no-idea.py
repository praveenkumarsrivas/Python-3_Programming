n, m = input().split()
n = int(n)
m = int(m)
narr = list(map(int, input().split()))
marr1 = set(map(int, input().split()))
marr2 = set(map(int, input().split()))
h=0
for i in narr:
    if i in marr1:
        h+=1
    if i in marr2:
        h-=1
print(h)

#note: here marr1 and marr2 is not a list it's a set because while it was list the time taken by the compiler is much as compared to set in

