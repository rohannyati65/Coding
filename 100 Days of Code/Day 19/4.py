# 2022. Convert 1D Array Into 2D Array (leetcode)
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (len(original) > (n * m)) or (len(original) < (n * m)):
            return []

        l = []
        a = 0
        for i in range(m):
            l1 = original[a : a + n]
            a = a + n
            l.append(l1)
        return l
