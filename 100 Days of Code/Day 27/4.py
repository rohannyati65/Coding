# Codeforces Round #751 (Div. 2), problem: (B) Divine Array (Runtime error on pretest 2)
t = int(input())
while t != 0:
    n = int(input())
    l = list(map(int, input().split()))
    lst = [[0]]
    lst.append(l)
    while lst[-1] != lst[-2]:
        l1 = []
        for i in lst[-1]:
            l1.append(lst[-1].count(i))
        lst.append(l1)
    lst.remove(lst[0])
    # print(lst)
    q = int(input())
    while q != 0:
        a, k = map(int, input().split())
        if k > len(lst):
            k = len(lst) - 1
        x = lst[k][a - 1]
        print(x)
        q = q - 1
    t = t - 1
