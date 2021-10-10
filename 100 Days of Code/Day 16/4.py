# 201. Bitwise AND of Numbers Range (leetcode)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left * 2 <= right:
            return 0

        x = left
        for i in range(left + 1, right + 1):
            x = x & i
        return x
