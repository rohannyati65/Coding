# Codeforces Round #751 (Div. 2), problem: (A) Two Subsequences
t=int(input())
while(t!=0):
    s=input()
    l=[i for i in s]
    l.sort()
    a=l[0]
    s=s.replace(a,'',1)
    print(a,s)
    t=t-1