# Save-the-Village
t = int(input())
while t != 0:
    n, z = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    count = 0
    a = 1
    while z > 0:
        z = z - l[-1]
        l[-1] = l[-1] // 2
        l.sort()
        count += 1
        if l[-1] == 0:
            a = 0
            break
    if a == 1:
        print(count)
    if a == 0:
        print("Run {}".format(z))
    t = t - 1
