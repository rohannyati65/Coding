# 451. Sort Characters By Frequency (leetcode)
class Solution:
    def frequencySort(self, s: str) -> str:
        l = [i for i in s]
        d = {}
        s = list(set(l))
        for i in s:
            d[i] = l.count(i)
        r = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        a = ""
        for i in range(len(r)):
            a = a + (r[i][0] * (l.count(r[i][0])))

        return a
