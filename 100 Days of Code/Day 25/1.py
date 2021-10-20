#  Contest Code:START16C
Problem Code:DIRECTN

t=int(input())
while(t!=0):
      n=int(input())
      s=input()
      l=[i for i in s]
      x='NO'
      for i in range(len(l)-2):
            for j in range(i+1,len(l)):
                  l1=l[i:j]
                  a=l1.count('L')
                  b=l1.count('R')
                  if(abs(a-b)>=2):
                        x='YES'
                        break
      print(x)
      t=t-1