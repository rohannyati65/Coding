# Secret Code (prepbyte)
t=int(input())
while(t!=0):
  s=input()
  a=""
  for i in s:
    if(i.isupper()):
      a=a+str(i)
  print(a)
  t=t-1



