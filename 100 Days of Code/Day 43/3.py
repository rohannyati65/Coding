# 989. Add to Array-Form of Integer (leetcode)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x = ""
        for i in num:
            x = x + str(i)

        x = str(int(x) + k)
        l = [int(i) for i in x]
        return l
