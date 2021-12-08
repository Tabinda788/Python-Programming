from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


# for k, c in groupby(input()):
#     # print("printing k ",k)
#     # print("printing c ",c)
#     # print("printing length of c ",len(list(c)))
#     # print("printing k again with type int",int(k))
#     # print((len(list(c)), int(k)))
#     print(*[(len(list(c)), int(k))])
#     pass