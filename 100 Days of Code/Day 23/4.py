# 191. Number of 1 Bits (leetcode)
class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        y = bin(n)[2:]
        # print(y)
        l = [str(i) for i in y]
        # print(l)
        return l.count("1")
