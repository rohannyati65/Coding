# 520. Detect Capital (leetcode)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0].isupper() == True:
            if word[1:].islower() == True:
                return True

            elif word[1:].isupper() == True:
                return True

            else:
                return False

        if word[0].islower() == True:
            if word[1:].islower() == True:
                return True

            return False
