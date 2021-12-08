# Sample Input

# Sorting1234

# Sample Output

# ginortS1324



s = sorted(input())
print(s)
lower = list(filter(lambda x: x.islower(),s))
print(lower)
upper = list(filter(lambda x: x.isupper(),s))
print(upper)
odd = list(filter(lambda x: x.isdigit() and int(x)%2 ==1, s))
print(odd)
even = list (filter(lambda x: x.isdigit() and int(x)%2 ==0,s))
print(even)
print(*(lower + upper+odd+even), sep = "")



a = "tabinda"
b = []
for i in a:
    b.append(str(i))

print(b)
print(list(filter(lambda x: x.islower(),b)))
