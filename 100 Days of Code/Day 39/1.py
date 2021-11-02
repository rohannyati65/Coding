# HackerEarth (Hiring Challenge)
# FIND MINIMUM SPEED TO THROW A BALL , CONSIDER A=10m/s^2
# Person standing at a height of Y meters from ground
# Tower at a height of Z meters from ground
# Distance between them is X meters
import math

T = int(input())
while T != 0:
    x, y, z = map(int, input().split())
    a = 10
    t = math.sqrt((2 * (y - z)) / a)
    s = x / t
    # if(len(str(s))<4):
    print("%.2f" % (round(s, 2)))
    # else:
    #    print(round(s,2))
    T = T - 1
