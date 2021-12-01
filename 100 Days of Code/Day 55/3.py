# Problem: S02E10 Contest: PRACTICE(SCHOOL) User: rohan_nyati
t = int(input())
while t != 0:
    n, x, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if abs(a[i] - b[i]) <= k:
            c += 1

    if c >= x:
        print("YES")
    else:
        print("NO")

    t = t - 1
