s = input()
l = list(s)
# print(l)
c = 1
res = ""
for i in range(len(l)):
    if i+1 < len(l) and l[i] == l[i + 1]:
        c += 1
    else:
        res = "(" + str(c) + ", " + str(l[i]) + ")"
        print(res, end=" ")
        c = 1
        i = i-1
