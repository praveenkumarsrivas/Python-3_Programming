n, m = input().split()
n = int(n)
m = int(m)
narr = list(map(int, input().split()))
marr1 = list(map(int, input().split()))
marr2 = list(map(int, input().split()))
inter_sec_happy = []
inter_sec_happy = list(set(narr) & set(marr1))
# print(inter_sec_happy)
h = 0
h = len(inter_sec_happy)

inter_sec_sad = []
inter_sec_sad = list(set(narr) & set(marr2))
# print(inter_sec_sad)
s = 0
s = len(inter_sec_sad)

happy = abs(h-s)

print(happy)
