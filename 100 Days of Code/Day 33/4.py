#  Contest Code:LTIME101C
# Problem Code:PROBCAT

t = int(input())
while t != 0:
    x = int(input())
    if x >= 1 and x < 100:
        print("Easy")
    if x >= 100 and x < 200:
        print("Medium")
    if x >= 200 and x <= 300:
        print("Hard")
    t = t - 1
