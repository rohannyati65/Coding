#  Contest Code:LTIME101C
# Problem Code:N1VALUES

t=int(input())
while(t!=0):
      n=int(input()) 
      if(n==1):
            print(*[1,1])
      else:
            x=2**n
            l=[i for i in range(1,n)]
            l.append(n-1)
            l.append(x-sum(l))
            print(*l)
      t=t-1



