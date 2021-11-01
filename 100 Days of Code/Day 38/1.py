# 389. Find the Difference (leetcode)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t

        s = [i for i in s]
        t = [i for i in t]

        l1 = list(set(s))
        l2 = list(set(t))

        l1.sort()
        l2.sort()
        x = ""

        for i in l2:
            a = t.count(i)
            b = s.count(i)
            if a != b:
                c = a - b
                # print(i)
                x = x + i * c
                break
        return x

        """
        x=""
        for i in range(len(t)):
            if(i>=len(s)):
                x=x+t[i]
            else:
        """
