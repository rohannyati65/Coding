# 1390. Four Divisors (leetcode)
import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            x = 1 + i
            y = 2
            for j in range(2, math.floor(math.sqrt(i)) + 1):
                if i % j == 0:
                    y = y + 1
                    x = x + j
                    if j != (i // j):
                        x = x + (i // j)
                        y += 1
                if y > 4:
                    break
            if y == 4:
                s = s + x

        return s
