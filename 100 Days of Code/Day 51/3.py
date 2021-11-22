# 455. Assign Cookies (leetcode)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        x = 0
        for i in g:
            if len(s) == 0:
                break
            else:
                for j in s:
                    if j >= i:
                        x = x + 1
                        s.remove(j)
                        break
        return x
