

n = int(input())
arr = input().split(" ")
print(all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr))


for i in arr:
    if i == i[::-1]:
        print("is palandrome",i)
    # print( i[::-1])
