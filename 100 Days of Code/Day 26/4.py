# 441. Arranging Coins (leetcode)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        a = 1
        while n >= a:
            n = n - a
            a = a + 1
        return a - 1
