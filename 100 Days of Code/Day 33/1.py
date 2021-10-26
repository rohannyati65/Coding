# F - Pair Sum Problem Code: RATRISUM
# 1st ATTEMPT (TLE)
t = int(input())
while t != 0:
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            x = abs(l[i] - l[j])
            s = s + x
    print(s)
    t = t - 1

# 2nd ATTEMPT
