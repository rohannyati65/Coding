# 1044. Longest Duplicate Substring (leetcode)
# 1st Attempt (TLE)
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        x = ""
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) + 1):
                y = s[i:j]
                if len(y) > 1:
                    if y in s[j - 1 :]:
                        if len(y) > len(x):
                            x = y
                else:
                    if y in s[j:]:
                        if len(y) > len(x):
                            x = y

                if len(x) == (len(s) // 2):
                    return x

        return x


# 2nd Attempt (Correct)
class Solution:
    def longestDupSubstring(self, s: str) -> str:

        # we do this for the cases when string is consisting  of a single letter, so we need to return string containing len(s)-1

        if s == s[::-1]:
            return s[:-1]

        x = ""
        first = 0
        last = len(s) - 1
        y = ""

        # Here we iterate over the entire list once and check several cases and update the value of x to contain the max substring

        while first <= last:
            y = y + s[first]
            # print(x,y)
            if len(y) > 1:
                if y in s[first:]:
                    if len(y) >= len(x):
                        x = y
                else:
                    if s[first] in s[first + 1 :]:
                        z = len(y)
                        i = 1
                        while i != (z):
                            if y[i:] in s[first:]:
                                y = y[i:]
                                break
                            i = i + 1

                    else:
                        y = ""

            else:
                if y in s[first + 1 :]:
                    if len(y) >= len(x):
                        x = y
                else:
                    if s[first] in s[first + 1 :]:
                        y = s[first]
                    else:
                        y = ""

            first = first + 1

        return x
