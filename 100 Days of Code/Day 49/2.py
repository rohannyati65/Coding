# 1160. Find Words That Can Be Formed by Characters (leetcode)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for i in words:
            if len(i) <= len(chars):
                l = [j for j in i]
                l1 = list(set(l))
                x = True
                for k in l1:
                    if (k not in chars) or (l.count(k) > chars.count(k)):
                        x = False
                        break

                if x == True:
                    count += len(i)
        return count
