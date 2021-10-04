# Ternary Palindromes (HackerEarth)
from itertools import permutations

t = int(input())
while t != 0:
    s = input()
    p = ["".join(p) for p in permutations(s)]
    # print(p)
    p = list(set(p))
    c = 0
    if len(p) % 2 == 0:
        p = list(p[: (len(p) // 2)])
    else:
        p = list(p[: (len(p) // 2) + 1])
    for i in p:
        c1 = 0
        for j in range(len(i)):
            for k in range(j + 1, len(i) + 1):
                a = i[j:k]
                b = a[::-1]
                if a == b:
                    c1 = c1 + 1
        if c1 <= len(i):
            c += 1
    print(c + c)

    t = t - 1
