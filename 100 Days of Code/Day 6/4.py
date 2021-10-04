# Deque Sorting (HackerEarth)

t = int(input())
while t != 0:
    n = int(input())
    l = list(map(int, input().split()))
    l1 = list(l)
    l1.sort()
    if l1 == l:
        print(0)
    else:
        c = 1
        for i in range(len(l) - 1):
            a = min(l[i + 1 :])
            if l[i] < a:
                c = c + 1

        print(len(l) - c)

    t = t - 1
