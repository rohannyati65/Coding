# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence (leetcode)
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = list(map(str, sentence.split()))
        x = len(searchWord)
        for i in range(len(l)):
            if len(l[i]) >= x:
                if l[i][:x] == searchWord:
                    return i + 1
        return -1
