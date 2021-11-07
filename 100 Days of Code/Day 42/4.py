# 66. Plus One (leetcode)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ""
        for i in digits:
            x = x + str(i)

        x = str(int(x) + 1)
        l = [int(i) for i in x]
        return l
