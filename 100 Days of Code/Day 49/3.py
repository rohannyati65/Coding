# 1047. Remove All Adjacent Duplicates In String (leetcode)
# In this code we compare the current value with the previous value .
# For better understanding remove the "#" commented part .
class Solution:
    def removeDuplicates(self, s: str) -> str:
        first = 1
        last = len(s)
        while first < last:
            if s[first] == s[first - 1]:
                s = s.replace(s[first - 1 : first + 1], "")
                if first > 1:
                    first = first - 1
            else:
                first += 1
            last = len(s)
            # print(s,first,last)
        return s
