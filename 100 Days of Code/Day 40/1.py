# HackerEarth (Hiring Challenge)
def solve(N, A, Q, query):
    l1 = []
    for j in query:
        l = list(A)
        left = j[1]
        right = j[2]
        if j[0] == 1:
            for i in range(left, right):
                l[i] = 1 - max(l[i], l[i - 1])

            x = l[right - 1]

        if j[0] == 2:
            for i in range(left, right):
                l[i] = 1 - min(l[i], l[i - 1])

            x = l[right - 1]
        l1.append(x)
    return l1

    # Write your code here
    # pass


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for i in range(Q)]

    out_ = solve(N, A, Q, query)
    print(" ".join(map(str, out_)))
