# 521. Longest Uncommon Subsequence I (leetcode)
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(b) > len(a):
            a, b = b, a

        if a != b:
            return len(a)

        for i in b:
            if i in a:
                a = a.replace(i, "", 1)
        if len(a) == 0:
            return -1

        return len(a)
