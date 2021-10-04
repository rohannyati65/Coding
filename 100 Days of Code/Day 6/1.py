# Likeable Array (Hackerearth)

import itertools
from itertools import repeat
t=int(input())
while(t!=0):
    n=int(input())
    l=list(map(int,input().split()))
    l1=list(set(l))
    c=0
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
            a=l.count(i)
            if(a!=i):
                if(a>i):
                    x=a-i
                    c=c+x
                
                if(i>a):
                    x=i-a
                    y=a
                    z=min(x,y)
                    c=c+z

    print(c)

    t=t-1
