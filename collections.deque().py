from collections import deque
# d = deque()
# d.append(1)
# print(d)
# d.appendleft(2)

# A deque is a double-ended queue. It can be used to add or remove elements 
# from both ends.

# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same
# O(1) performance in either direction.
d = deque()
# print(d)
for _ in range(int(input())):
    cmd, *args = input().split()
    # print(cmd)
    print("printing args",*args)
    getattr(d, cmd)(*args)
# print(getattr(d,cmd))
# print(d)
[print(x, end=' ') for x in d]