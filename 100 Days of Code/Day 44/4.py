# 125. Valid Palindrome (leetcode)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ""
        for i in s:
            if i.isalpha():
                l = l + i.lower()

            if i.isnumeric():
                l = l + i
        # print(l)
        if l == l[::-1]:
            return True

        return False
