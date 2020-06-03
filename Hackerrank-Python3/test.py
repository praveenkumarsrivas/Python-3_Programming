inp = [[1, 2, 3, 4, 5, 6], [3, 2, 1, 4, 5, 6],
       [4, 3, 2, 1, 5, 6], [1, 1, 1, 1, 1, 1]]
out = [max(s) for s in zip(*inp)]
print(out)
