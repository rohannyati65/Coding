# Permutations
#result = []
#x=0
def permute(data, i, length):
    if i == length:
        if(data==l1):
            #x=x+1
        #print(data)
            result.append(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]
#permute(list(ini_str), 0, len(ini_str))


#import itertools
t=int(input())
while(t!=0):
    n=int(input())
    s=input()
    q=int(input())
    for i in range(q):
        result=[]
        l,r=map(int,input().split())
        s1=s[l-1:r]
        l1=[i for i in s1]
        l1.sort()
        permute(list(s1), 0, len(s1))
        y=len(result)
        #get_permutation(s1,l1)
        #print(x)
        #print(x)
        print((y)%((10^9)+7))
 
    t=t-1
 
