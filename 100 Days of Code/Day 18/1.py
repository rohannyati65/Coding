#  Division Problem Code: DIVEO
import math        
t=int(input())

lst=[]
for i in range(1,(10^9)+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        lst.append(i)
#print(lst)

while(t!=0):
    n,a,b=map(int,input().split())
    p=0
    while(n>1):
        if n in lst:
            if(n%2==0):
                p=p+a
            else:
                p=p+b
            break
            
        if(n%2==0):
            x=2
            p=p+a
            
        elif(n%3==0):
            x=3
            p=p+b
            
        elif(n%5==0):
            x=5
            p=p+b
            
        elif(n%7==0):
            x=7
            p=p+b 
            
        #print(n,x,p)
        n=int(n/x)
    
    if(n%2==0):
        y=a
    else:
        y=b
        
    print(max([y,p]))
    t=t-1




