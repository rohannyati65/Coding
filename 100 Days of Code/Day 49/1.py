# 884. Uncommon Words from Two Sentences (leetcode)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = list(map(str, s1.split()))
        l2 = list(map(str, s2.split()))

        l = []

        for i in l1:
            if i not in l2 and l1.count(i) == 1:
                l.append(i)

        for i in l2:
            if i not in l1 and l2.count(i) == 1:
                l.append(i)

        return l
