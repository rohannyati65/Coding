# 1657. Determine if Two Strings Are Close (leetcode)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        l1 = [i for i in word1]
        l2 = [i for i in word2]
        s1 = list(set(l1))
        s2 = list(set(l2))
        l3 = []
        for i in s2:
            l3.append(l2.count(i))
            if i not in s1:
                return False
        l4 = []
        for i in s1:
            l4.append(l1.count(i))
            if i not in s2:
                return False
        l3.sort()
        l4.sort()
        if l3 != l4:
            return False

        return True
