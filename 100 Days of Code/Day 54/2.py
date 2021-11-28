# 2085. Count Common Words With One Occurrence (leetcode)
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        if len(words2) > len(words1):
            words1, words2 = words2, words1
        x = 0
        for i in words1:
            if words1.count(i) == 1 and words2.count(i) == 1:
                x += 1
        return x
