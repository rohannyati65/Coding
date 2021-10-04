# Container With Most Water (gfg)


def maxArea(A, le):

    l = 0
    r = le - 1
    area = 0
    while l < r:
        area = max(area, min(A[l], A[r]) * (r - l))
        if A[l] < A[r]:
            l += 1
        else:
            r = r - 1

    return area
