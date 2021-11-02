# 459. Repeated Substring Pattern (leetcode)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 1
        while i != (len(s) // 2) + 1:
            x = s[:i]
            i = i + 1
            y = s.count(x)
            # print(x,y)
            if y * len(x) == len(s):
                return True

        return False
