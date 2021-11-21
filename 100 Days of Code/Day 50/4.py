# 2078. Two Furthest Houses With Different Colors (leetcode)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        x = 0
        first = 0
        last = len(colors) - 1
        while first < last:
            if colors[first] != colors[last]:
                x = max(x, last - first)
            last = last - 1

        first = 0
        last = len(colors) - 1
        while first < last:
            if colors[first] != colors[last]:
                x = max(x, last - first)
            first += 1

        return x
