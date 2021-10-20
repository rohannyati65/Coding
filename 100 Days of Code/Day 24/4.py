#  Contest Code:START16C
Problem Code:HCAGMAM1

t=int(input())
while(t!=0):
      x,y=map(int,input().split())
      s=input()
      l=[i for i in s]
      a=0
      b=0
      l1=[]
      for i in range(len(l)):
            if(l[i]=='0'):
                  if(a==0):
                        pass
                  else:
                        l1.append(a)
                  a=0
            else:
                  b=b+1
                  a=a+1
      l1.append(a)
      
            #print(l1)
      c=max(l1)
      #print(b,c)
      z=(x*b)+(y*c)
      print(z)
      t=t-1
      