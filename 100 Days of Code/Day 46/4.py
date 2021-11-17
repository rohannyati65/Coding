# 2070. Most Beautiful Item for Each Query (leetcode)
# TLE
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        p = []
        b = []
        for i in items:
            p.append(i[0])
            b.append(i[1])

        l = []
        for i in queries:
            l1 = []
            for j in range(len(p)):
                if p[j] <= i:
                    l1.append(b[j])

            if len(l1) == 0:
                l.append(0)
            else:
                l.append(max(l1))

        return l


# TLE
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        l = []
        for i in queries:
            a = 0
            for j in range(len(items)):
                if items[j][0] <= i:
                    if items[j][1] > a:
                        a = items[j][1]

            l.append(a)
        return l
