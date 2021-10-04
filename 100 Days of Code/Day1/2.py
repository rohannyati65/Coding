# Nearly Sorted Algorithm (gfg)

t = int(input())
while t != 0:
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    print(*l)
    t = t - 1
