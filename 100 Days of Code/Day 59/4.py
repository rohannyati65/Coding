# 121. Best Time to Buy and Sell Stock (leetcode)
# 1st Method (TLE)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        for i in range(len(prices) - 1):
            x = prices[i]
            y = max(prices[i:])
            if y - x > a:
                a = y - x
        return a


# 2nd Methode (ACCEPTED)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        y = max(prices)
        for i in range(len(prices)):
            x = prices[i]
            y = min(y, x)
            z = x - y
            p = max(p, z)
        return p
