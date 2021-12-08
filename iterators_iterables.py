from itertools import combinations
N=int(input())
n=input().split()
K=int(input())

# letters ="GeEKS"
  
# # size of combination is set to 3
# a = combinations(letters, 3) 
# y = [' '.join(i) for i in a]
# print(y)

x=combinations(''.join(n),K)
# print(''.join(n))
# print(x)
count_total,count_a=0,0
for i in x:
    # print(i)
    count_total+=1
    if 'a' in i:
        count_a+=1
print(round(count_a/count_total,3))
