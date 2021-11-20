# 1935. Maximum Number of Words You Can Type (leetcode)
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = list(map(str, text.split()))
        count = 0
        for i in l:
            flag = True
            for j in i:
                if j in brokenLetters:
                    flag = False
                    break
            if flag == True:
                count += 1
        return count
