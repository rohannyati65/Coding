# Count Pairs (PrepBytes)
import itertools
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

l=[i for i in range(n)]
lst=list(map(list,itertools.combinations(l,2)))
count=0
for i in lst:
  x=i[0]
  y=i[1]
  if(a[x]==b[c[y]]):
    count+=1
print(count)

