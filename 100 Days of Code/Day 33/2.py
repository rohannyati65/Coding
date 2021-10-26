# C - Alex and Integer Problem Code: RATRIPRIME
# 1st ATTEMPT(WRONG)
t = int(input())
while t != 0:
    n = int(input())
    y = 0
    for i in range(1, (10 ** 7)):
        x = n * i + 1
        if (x % 2 == 0 or x % 3 == 0) and x != 2 and x != 3:
            y = 1
            print(i)
            break
        else:
            pass
    if y == 0:
        print(-1)
    t = t - 1
