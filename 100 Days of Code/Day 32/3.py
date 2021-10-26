# B - Count Unique Elements Problem Code: RATRIUNIQUE
t = int(input())
while t != 0:
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = list(set(l))
    c = 0
    for i in l:
        if i > k:
            c += 1

    print(c)
    t = t - 1
