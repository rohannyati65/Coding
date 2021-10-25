# 1893. Check if All the Integers in a Range Are Covered (leetcode)
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        l = []
        for i in ranges:
            l1 = [i for i in range(i[0], i[1] + 1)]
            l = l + l1

        for i in range(left, right + 1):
            if i not in l:
                return False
        return True
