import numpy
# array = []
# n, m = map(int, input().split())
# for _ in range(n): 
#     array.append(list(map(int, input().split())))
#     array = numpy.array(array,int)
#     print(numpy.mean(array, axis=1))
#     print(numpy.var(array, axis=0))
#     print(round(numpy.std(array), 11))



N, M = map(int, input().strip().split())

my_array = numpy.array([ input().strip().split() for _ in range(N) ], int)

print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None),11))