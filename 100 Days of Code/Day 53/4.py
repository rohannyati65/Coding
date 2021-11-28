# Problem: CSTOCK Contest: LTIME102C User: rohan_nyati
t = int(input())
while t != 0:
    s1, a, b, c1 = map(int, input().split())
    x = s1 + ((s1 * c1) // 100)
    if x in range(a, b + 1):
        print("YES")
    else:
        print("NO")
    t = t - 1
