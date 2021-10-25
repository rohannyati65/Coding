# 1816. Truncate Sentence (leetcode)
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = list(map(str, s.split()))
        l = l[:k]
        a = ""
        for i in range(len(l)):
            if i == len(l) - 1:
                a = a + l[i]

            else:
                a = a + l[i] + " "

        return a
