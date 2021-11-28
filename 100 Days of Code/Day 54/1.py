# Problem: STRGMNZ Contest: LTIME102C
import math

t = int(input())
while t != 0:
    n = int(input())
    x1 = n
    y1 = 10 ** 6 + 1
    for i in range(n + 1, n * 2):
        if i % n != 0:
            z = abs(math.gcd(n, i) - ((n * i) // (math.gcd(n, i))))
            b = min(y1, z)
            if b < y1:
                y1 = b
                x1 = i
    print(x1)
    t = t - 1
