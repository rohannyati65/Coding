# Contest Code:PRACTICE Problem Code:DDCW1_01
t = int(input())
while t != 0:
    a, b, c, n = map(int, input().split())
    l = [a, b, c]
    while len(l) != n:
        x = l[-1] + l[-2] + l[-3]
        l.append(x)
    print((l[-1]) % (1000000007))
    t = t - 1
