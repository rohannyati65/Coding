# 13. Roman to Integer (leetcode)
class Solution:
    def romanToInt(self, s: str) -> int:
        l = [1, 5, 10, 50, 100, 500, 1000]
        y = s[::-1]
        lst = ["I", "V", "X", "L", "C", "D", "M"]
        count = l[lst.index(y[0])]
        for i in range(1, len(y)):
            if l[lst.index(y[i])] >= l[lst.index(y[i - 1])]:
                count += l[lst.index(y[i])]

            else:
                count = count - l[lst.index(y[i])]
        return count
