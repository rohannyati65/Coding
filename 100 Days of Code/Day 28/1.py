# 1832. Check if the Sentence Is Pangram (leetcode)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = [i for i in sentence]
        l = list(set(l))
        if len(l) == 26:
            return True
        return False
