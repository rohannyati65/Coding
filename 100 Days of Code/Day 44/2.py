# 1413. Minimum Value to Get Positive Step by Step Sum (leetcode)
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        a = 1
        x = False
        while x != True:
            # print(a)
            y = a
            x = True
            for i in nums:
                y = y + i
                if y < 1:
                    x = False
                    break

            if x == False:
                a = a + 1
        return a
