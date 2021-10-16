# HackerEarth (October Circuit's 21)
t = int(input())
while t != 0:
    s = input()
    lst = [i for i in s]
    l = lst.count("L")
    r = lst.count("R")
    u = lst.count("U")
    d = lst.count("D")
    x = abs(l - r)
    y = abs(u - d)
    if x % 2 != 0:
        a = (x // 2) + 1
    if x % 2 == 0:
        a = x // 2
    if y % 2 != 0:
        b = (y // 2) + 1
    if y % 2 == 0:
        b = y // 2

    print(a + b)
    t = t - 1
