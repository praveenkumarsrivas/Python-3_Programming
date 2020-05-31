import numpy
A = numpy.array([int(x) for x in input().split(" ")])
B = numpy.array([int(x) for x in input().split(" ")])
print(numpy.inner(A, B))
print(numpy.outer(A, B))
