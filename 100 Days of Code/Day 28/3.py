# 2000. Reverse Prefix of Word (leetcode)
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                x = word[: i + 1]
                word = x[::-1] + word[i + 1 :]
                break
        return word
