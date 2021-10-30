# 5900. Plates Between Candles (leetcode)

# 1st Attempt (TLE)


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        l1 = []
        for i in queries:
            l = i[0]
            r = i[1]
            x = s[l : r + 1]
            if "*" not in x:
                c = 0

            elif "|" not in x:
                c = 0

            else:
                y = x.count("|")
                a = x.index("|")
                z = x[::-1]
                b = z.index("|")
                c = len(x)
                c = c - b
                c = c - a
                c = c - y
            l1.append(c)
        return l1
