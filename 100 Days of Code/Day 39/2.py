# 434. Number of Segments in a String (leetcode)
class Solution:
    def countSegments(self, s: str) -> int:
        l = list(map(str, s.split()))
        return len(l)
