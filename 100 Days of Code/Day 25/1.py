#  Contest Code:START16C
Problem Code:DIRECTN

"Correct"
t=int(input())
while(t!=0):
      n=int(input())
      s=input()
      l=[i for i in s]
      x='NO'
      for i in range(len(l)-1):
            y=l[i:i+2]
            if((y.count('L')==2) or (y.count('R')==2)):
                  x='YES'
                  break
            
      print(x)
      t=t-1

"GIVES TLE"
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