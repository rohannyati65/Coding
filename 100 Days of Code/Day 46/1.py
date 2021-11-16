# 2068. Check Whether Two Strings are Almost Equivalent (leetcode)
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for i in range(len(word1)):
            a = word1.count(word1[i])
            b = word2.count(word1[i])
            if abs(a - b) > 3:
                return False

        for i in range(len(word2)):
            a = word2.count(word2[i])
            b = word1.count(word2[i])
            if abs(a - b) > 3:
                return False

        return True
