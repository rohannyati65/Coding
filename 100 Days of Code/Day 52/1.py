# Problem: MAKEEQUAL Contest: START18C
t = int(input())
while t != 0:
    n = int(input())
    l = list(map(int, input().split()))
    if l.count(l[0]) == len(l):
        print(0)
    else:
        x = max(l)
        y = min(l)
        print(x - y)
    t = t - 1
