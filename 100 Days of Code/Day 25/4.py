# Dance Moves
t = int(input())
while t != 0:
    x, y = map(int, input().split())
    z = abs(y - x)
    if y > x:
        if z % 2 == 0:
            a = z // 2
        else:
            a = (z // 2) + 1

        x = x + (a * 2)
        b = abs(y - x)
        print(a + b)
    else:
        print(z)
    t = t - 1
