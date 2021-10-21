# Input queries (October Circuits '21)
t = int(input())
while t != 0:
    l, r, k = map(int, input().split())
    left = r - k + 1
    right = r
    if left == 1:
        if right == 1:
            print(1)
        else:
            print(0)
    elif left == 0:
        print(0)
    else:
        i = right - 1
        while i >= left and right != 0:
            right = right & i
            i = right - 1
        print(right)
    t = t - 1
