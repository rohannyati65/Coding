# Round G 2021 (Dogs and Cats)
t = int(input())
while t != 0:
    n, d, c, m = map(int, input().split())
    s = input()
    y = "YES"
    for i in range(len(s)):
        if s[i] == "D":
            if d == 0:
                y = "NO"
                break
            d = d - 1
            c = c + m

        else:
            if c == 0:
                if s[i:].find("D") == True:
                    y = "NO"
                break
            c = c - 1
    print(y)
    t = t - 1
