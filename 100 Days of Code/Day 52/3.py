# 986. Interval List Intersections (leetcode)
class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        l = []
        if len(firstList) != 0:
            for i in firstList:
                if len(secondList) != 0:
                    for j in secondList:
                        if i[0] == j[1]:
                            if [i[0], i[0]] not in l:
                                l.append([i[0], i[0]])
                        elif i[1] == j[0]:
                            if [i[1], i[1]] not in l:
                                l.append([i[1], i[1]])
                        else:
                            if (i[0] in range(j[0], j[1] + 1)) or (
                                j[0] in range(i[0], i[1] + 1)
                            ):
                                if [max(i[0], j[0]), min(i[1], j[1])] not in l:
                                    l.append([max(i[0], j[0]), min(i[1], j[1])])
        return l
