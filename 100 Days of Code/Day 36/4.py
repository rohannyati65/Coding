# Contest Code:SNCK1B21 Problem Code:QPLACE
t = int(input())
while t != 0:
    N = int(input())
    z = N
    q = N - 2
    l = []
    if N > 3:
        x = N - 3
        for i in range(x):
            l1 = "." * (N - i - 1)
            l1 = l1 + "Q"
            l2 = "." * (i)
            l1 = l1 + l2
            l.append(l1)
        N = 3

    if N == 3:
        l1 = "." * z
        l.append(l1)
        N = N - 1

    if N == 2:
        l1 = ".Q"
        l2 = "." * (z - 2)
        l1 = l1 + l2
        l.append(l1)
        N = N - 1

    if N == 1:
        l1 = "." * z
        l.append(l1)
        N = N - 1

    for i in l:
        print(i)
    t = t - 1
