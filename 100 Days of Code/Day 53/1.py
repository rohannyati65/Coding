# Codeforces Round #756 (Div. 3), problem: (A) Make Even, Accepted
t = int(input())
while t != 0:
    n = int(input())
    n = str(n)
    if int(n[-1]) % 2 == 0:
        print(0)

    elif int(n[0]) % 2 == 0:
        print(1)

    else:
        x = 0
        for i in range(len(n)):
            if int(n[i]) % 2 == 0:
                x = x + 1
                break

        if x == 0:
            print(-1)
        else:
            print(x + 1)

    t = t - 1
