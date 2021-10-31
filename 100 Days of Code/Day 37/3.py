# Contest Code:IICP2021 Problem Code:KILLFEED

t = int(input())
while t != 0:
    n = int(input())
    l = list(map(int, input().split()))
    y = sum(l)
    z = max(l)
    print(y - z)
    t = t - 1
