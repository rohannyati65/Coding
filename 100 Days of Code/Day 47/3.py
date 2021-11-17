# Problem: NEWPIECE Contest: START17C
t = int(input())
while t != 0:
    x, y, a, b = map(int, input().split())
    if x == a and y == b:
        print(0)

    else:
        s = 0
        if (x + y) % 2 == 0:
            s = 1

        f = 0
        if (a + b) % 2 == 0:
            f = 1

        if f == s:
            print(2)

        else:
            print(1)

    t = t - 1
