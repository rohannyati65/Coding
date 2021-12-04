# Mike's intelligence
t = int(input())
while t != 0:
    x = int(input())
    y = 1
    z = 0
    for i in range(1, x + 1):
        y = y * i
        z = z + i

    if y % z == 0:
        print("EURIKA")
    else:
        print("HELL NO")
    t = t - 1
