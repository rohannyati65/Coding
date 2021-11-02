# HackerEarth (Hiring Challenge)
def solve (N, X, Y, A, B):
    s=0
    for i in range(len(A)):
        a=A[i]
        for j in range(len(B)):
            b=B[j]
            if(((a^b)&X)==((a^b)&Y)):
                s=s+1
    return(s)
    # Write your code here
    #pass

T = int(input())
for _ in range(T):
    N = int(input())
    X = int(input())
    Y = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    out_ = solve(N, X, Y, A, B)
    print (out_)