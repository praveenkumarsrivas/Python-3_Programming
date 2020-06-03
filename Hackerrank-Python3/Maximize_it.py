from itertools import product
# k, m = list(map(int, input().split()))
# inp = []
# for i in range(k):
#     l = input()
#     l = l.split(" ")
#     if '' in l:
#         l.remove('')
#     l = [int(x) for x in l]
#     inp.append(l[1:])
# print(inp)
# e = 0
# res = 0

# res = map(lambda x: sum(i**2 for i in x) % m, product(*l))


# # for i in inp:
# #     # print(i)
# #     e = max(i)
# #     # (A + B) mod C = (A mod C + B mod C) mod C
# #     res = (res % m+(e * e) % m) % m
# #     e = 0
# print(max(res))

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x) % M, product(*N))
print(max(results))


