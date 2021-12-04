# All-possibilities
import itertools

n = int(input())
x = str(n)
l1 = [i for i in x]
l = list(map(list, itertools.permutations(l1, len(l1))))
# print(l)
l2 = []
for i in l:
    y = ""
    for j in i:
        y = y + j
    if int(y) not in l2:
        l2.append(int(y))
l2.sort()
for i in l2:
    print(i)
