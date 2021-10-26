# D - Another Bracket Problem Problem Code: RATRIBRACKET
# 1st ATTEMPT (WRONG)
t = int(input())
while t != 0:
    s = input()
    lst = [i for i in s]
    o = ["(", "[", "{"]
    c = [")", "]", "}"]
    a = 0
    b = 0
    for i in s:
        if i in o:
            a += 1
        else:
            b += 1
    if a == b:
        print("YES")
    else:
        print("NO")
    t = t - 1

# 2nd ATTEMPT(CORRECT)
t = int(input())
while t != 0:
    s = input()
    lst = [i for i in s]
    o = ["(", "[", "{"]
    a = 0
    for i in s:
        if i in o:
            a = a + 1
        else:
            a = a - 1

        if a < 0:
            break
    if a == 0:
        print("YES")
    else:
        print("NO")
    t = t - 1
