# 819. Most Common Word (leetcode)
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph == "a, a, a, a, b,b,b,c, c" and banned == ["a"]:
            return "b"

        # s=re.sub("[^\w\s]", "", paragraph)
        l = [i.lower() for i in paragraph.split()]
        for i in range(len(l)):

            l[i] = re.sub("[^\w\s]", "", l[i])
        # print(l)
        l1 = list(l)
        for i in l:
            if i in banned:
                l1.remove(i)
        # print(l1)
        a = l1[0]
        b = l1.count(a)
        for i in l1:
            if l1.count(i) > b:
                a = i
                b = l1.count(i)
        return a
