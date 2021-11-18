# 806. Number of Lines To Write String (leetcode)
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        x = 1
        s1 = 0
        for i in s:
            a = l.index(i)
            if s1 + widths[a] > 100:
                s1 = widths[a]
                x += 1
            else:
                s1 = s1 + widths[a]
        return [x, s1]
