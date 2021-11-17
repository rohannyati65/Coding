#  Contest Code:START17C
# Problem Code:CHEFVACATION

t = int(input())
while t != 0:
    x, y, z = map(int, input().split())
    if x + y <= z:
        print("YES")
    else:
        print("NO")
    t = t - 1
