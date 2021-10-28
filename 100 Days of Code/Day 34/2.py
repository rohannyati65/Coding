# 1859. Sorting the Sentence (leetcode)
class Solution:
    def sortSentence(self, s: str) -> str:
        l = list(map(str, s.split()))
        l1 = []
        for i in range(len(l)):
            x = l[i][-1]
            l1.append(int(x))
            l[i] = l[i][:-1]
        # print(l,l1)
        y = len(l1)
        a = ""
        for i in range(1, y + 1):
            x = l1.index(i)
            if i == y:
                a = a + l[x]
            else:
                a = a + l[x] + " "

        return a
