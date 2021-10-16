# Problem Code: TESTSERIES
t = int(input())
while t != 0:
    l = list(map(int, input().split()))
    I = l.count(1)
    E = l.count(2)
    if I > E:
        print("INDIA")

    elif E > I:
        print("ENGLAND")

    else:
        print("DRAW")

    t = t - 1
