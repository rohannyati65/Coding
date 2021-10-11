# 567. Permutation in String (leetcode)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ordered = ''.join(sorted(s1))
        for index in range(0, len(s2) - len(s1) + 1):
            s = s2[index:(index+len(s1))]
            s = ''.join(sorted(s))
            if s == ordered:
                return True
        return False