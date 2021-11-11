# 49. Group Anagrams (leetcode)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        for i in strs:
            a = [j for j in i]
            a.sort()
            if a not in l:
                l.append(a)

        # print(l)
        l1 = [[]] * (len(l))
        # print(l1)
        for i in strs:
            a = [j for j in i]
            a.sort()
            b = l.index(a)
            # print(b)
            x = [i]
            l1[b] = l1[b] + x
            # l1[b].append(i)
            # print(l1)

        return l1
