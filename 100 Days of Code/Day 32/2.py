# A - Bob and Strings Problem Code: RATRICOMP
import string
l=list(string.ascii_lowercase)
a=input()
a=a.lower()
b=input()
b=b.lower()
z=0
for i in range(len(a)):
      x=l.index(a[i])
      y=l.index(b[i])
      if(x>y):
            z=1
            print("GREATER")
            break
      elif(y>x):
            z=1
            print("SMALLER")
            break
if(z==0):
      print("EQUAL")
