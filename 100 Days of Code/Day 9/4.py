# 70. Climbing Stairs (leetcode)
class Solution:
    def climbStairs(self, n: int) -> int:
        f = 0
        s = 1
        for i in range(n):
            c = f + s
            f = s
            s = c
        return c
