# 1003. Check If Word Is Valid After Substitutions (leetcode)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3 != 0:
            return False

        while len(s) != 0:
            if "abc" in s:
                s = s.replace("abc", "")

            else:
                return False

        return True
