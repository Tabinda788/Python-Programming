from collections import OrderedDict
words = OrderedDict()
# print(words)
for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1
    # print(words)
# print(words) 
print(len(words))
print(*words.values())