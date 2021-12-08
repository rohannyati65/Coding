# 5. Longest Palindromic Substring (leetcode)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if s == s[::-1]:
            return s
        else:
            c = s[0]
            for i in range(len(s)):
                x = ""
                for j in s[i:]:
                    x = x + j
                    y = x[::-1]
                    if x == y:
                        if len(x) > len(c):
                            c = x
            return c
