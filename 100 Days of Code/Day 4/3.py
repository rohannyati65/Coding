# Newton's coding challenge September 2021 - Love for Subsets

# 1nd attempt
import itertools

t = int(input())
while t != 0:
    n = int(input())
    if n < 3:
        print(1)
    else:
        l = [i for i in range(1, n + 1)]
        # print(l)
        l1 = []
        for i in range(2, n):
            l2 = list(map(list, itertools.combinations(l, i)))
            l1 = l1 + l2
        l1.sort(key=len)
        # print(l1)
        x = 2
        for i in l1[::-1]:
            # print(i)
            for j in range(len(i) // 2):
                if (i[j] * 2) not in i:
                    x = 0
                else:
                    x = 1
                    break
            if x == 0:
                print(len(i))
                break
        if x == 1:
            print(1)
    t = t - 1

# 2nd attempt

t = int(input())
while t != 0:
    n = int(input())
    if n < 3:
        print(1)
    else:
        l1 = []
        for i in range(1, n + 1):
            if i % 2 != 0:
                l1.append(i)
            else:
                if ((i * 2) not in l1) and ((i / 2) not in l1):
                    l1.append(i)

        print(len(l1))

    t = t - 1
