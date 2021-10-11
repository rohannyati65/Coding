# 3. Longest Substring Without Repeating Characters (leetcode)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        if s == "":
            return 0
        if s == " ":
            return 1
        if len(s) == 1:
            return 1
        else:
            for i in range(len(s)):
                l1 = []
                x = str(s[i:])
                for j in x:
                    if j not in l1:
                        l1.append(j)
                    elif j in l1:
                        break
                l.append(len(l1))

            r = str(s[::-1])
            for i in range(len(r)):
                l1 = []
                x = str(r[i:])
                for j in x:
                    if j not in l1:
                        l1.append(j)
                    elif j in l1:
                        break
                l.append(len(l1))

            return max(l)
