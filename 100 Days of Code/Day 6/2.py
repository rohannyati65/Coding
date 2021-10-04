# Good Strings (HackerEarth)

t = int(input())
while t != 0:
    n = int(input())
    l = []
    for i in range(n):
        a = input()
        l.append(a)

    # print(l)
    lst = []
    count = 0
    for i in range(len(l) - 1):
        for j in l[i + 1 :]:
            if ("0" in l[i]) and ("0" in j):
                count += 1

            elif ("1" in l[i]) and ("1" in j):
                count += 1

    print(count)
    t = t - 1
