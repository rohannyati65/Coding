#  Permutations (October Circuits '21)
def Factorial(n):
    if(n==0 or n==1):
        return(1)
    
    return((n)*Factorial(n-1))
 
t=int(input())
while(t!=0):
    n=int(input())
    s=input()
    q=int(input())
    for i in range(q):
        l,r=map(int,input().split())
        s1=s[l-1:r]
        l1=[i for i in s1]
        #l1.sort()
        #s2=""
        l2=list(set(l1))
        x=1
        for i in l2:
            y=l1.count(i)
            if(y>1):
                z=Factorial(y)
                #print(z)
                x=x*z
                #print(x)
        if(((x)%((10**9)+7))==0):
            print(1)
        else:
            print((x)%((10**9)+7))
 
    t=t-1

