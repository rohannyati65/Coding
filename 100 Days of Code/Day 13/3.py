# 557. Reverse Words in a String III (leetcode)
class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(map(str, s.split()))
        # print(l)
        p = ""
        x = " "
        for i in range(len(l)):
            a = l[i]
            if i == (len(l) - 1):
                p = p + a[::-1]
            else:
                p = p + a[::-1] + x
        return p
