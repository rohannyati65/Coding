# 1071. Greatest Common Divisor of Strings (leetcode)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1

        l = []
        for i in range(len(str2)):
            for j in range(i + 1, len(str2) + 1):
                a = str2[i:j]
                l.append(a)
        l.sort(key=len)
        l = l[::-1]
        # print(l)
        x = ""
        for i in l:
            if i in str1:
                a = str1.count(i)
                b = str2.count(i)
                if len(str1) == (len(i) * a) and (len(str2) == (len(i) * b)):
                    x = i
                    break
        return x
