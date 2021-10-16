# Problem Code: LUCKYNUM
t = int(input())
while t != 0:
    a, b, c = map(int, input().split())
    x = 0
    if a == 7 or b == 7 or c == 7:
        x = 1
    if x == 1:
        print("YES")
    if x == 0:
        print("NO")

    t = t - 1
