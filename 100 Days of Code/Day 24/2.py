# 151. Reverse Words in a String (leetcode)
class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        a = ""
        for i in range(len(s)):
            if s[i] == " ":
                if len(a) > 0:
                    l.append(a)
                a = ""
                pass
            else:
                a = a + s[i]
        if len(a) > 0:
            l.append(a)
        # print(l)
        l = l[::-1]
        # print(l)
        return " ".join(l)
