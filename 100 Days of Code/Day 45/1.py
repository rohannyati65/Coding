# HackerEarth
t = int(input())
while t != 0:
    n = int(input())
    l = [int(i) for i in str(n)]
    l.sort()
    a = ""
    b = ""
    for i in range(len(l)):
        if i % 2 == 0:
            a = a + str(l[i])
        else:
            b = b + str(l[i])
    c = int(a) + int(b)
    print(c)
    t = t - 1
