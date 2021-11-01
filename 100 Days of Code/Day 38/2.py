# 345. Reverse Vowels of a String (leetcode)
class Solution:
    def reverseVowels(self, s: str) -> str:
        x = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = [i for i in s]
        s1 = s[::-1]
        l = []
        for i in s1:
            if i in x:
                l.append(i)

        a = 0
        y = ""
        for i in range(len(s)):
            if s[i] in x:
                y = y + l[a]
                a = a + 1
            else:
                y = y + s[i]
        return y
