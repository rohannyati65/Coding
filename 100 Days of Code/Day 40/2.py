# Codeforces Round #753 (Div. 3), problem: (A) Linear Keyboard
t = int(input())
while t != 0:
    s1 = input()
    l = [i for i in s1]
    s2 = input()
    s3 = [i for i in s2]

    # s3=list(set(s))
    l1 = []
    for i in s3:
        # if l.index(i)+1 not in l1:
        l1.append(l.index(i) + 1)
    # print(l1)
    x = 0
    # l1.sort()
    # print(l1)
    for i in range(1, len(l1)):
        z = abs(l1[i] - l1[i - 1])
        x = x + z
    print(x)
    t = t - 1
