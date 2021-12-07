# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 

# o/p
# 206

# m= list(input().split())
# n =int(m[0])
# d =int(m[1])
# # print(d)

# emp = []
# for i in range(int(n)):
#     lis = list(input().split())
#     m = max(lis)
#     # print(int(m))
#     sq = int(m)**2
#     emp.append(sq)
# print(emp)
# s = 0
# for i in emp:
#     s += int(i)
# print(s%d)

# https://www.thepoorcoder.com/hackerrank-maximize-it-solution/

# (52 + 92 + 10 2)%1000 =206

# (52 %1000 + 92 %1000 + 10 2 %1000) %1000 =206%1000 = 206
from itertools import product

K,M = map(int,input().split())
# THis is a generator
N = (list(map(int, input().split()))[1:] for _ in range(K))  
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))


# K,M = map(int,input().split())
# nums = []
# for _ in range(K):
#     # We use map and split function to convert the row input into list of integers.
#     row = map(int,input().split()[1:])
#     # print(row)
#     nums.append(map(lambda x:x**2%M, row))
# print(nums)

# a,b,c = input.split()