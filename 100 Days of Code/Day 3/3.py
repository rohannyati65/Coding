# k largest elements (gfg)


class Solution:
    def kLargest(self, arr, n, k):
        arr.sort()
        a = arr[-k:]
        return a[::-1]
