# 2062. Count Vowel Substrings of a String (leetcode)
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        l = ["a", "e", "i", "o", "u"]
        x = 0
        for i in range(len(word) - 4):
            for j in range(i + 5, len(word) + 1):
                y = word[i:j]
                l1 = [z for z in y]
                s1 = list(set(l1))
                s1.sort()
                # print(y)
                if s1 == l:
                    # print(y)
                    x = x + 1
        return x
