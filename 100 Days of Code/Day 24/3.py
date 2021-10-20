#   Contest Code:START16C
Problem Code:PASSORFAIL

t=int(input())
while(t!=0):
      n,x,p=map(int,input().split())
      a=n-x
      if(((x*3)-a)>=p):
            print("PASS")
      else:
            print("FAIL")
      t=t-1

