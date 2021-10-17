# 2042. Check if Numbers Are Ascending in a Sentence (leetcode)
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = list(map(str, s.split()))
        # print(l)
        l1 = []
        for i in l:
            if i.isnumeric() == True:
                l1.append(int(i))
        # print(l1)
        s1 = list(set(l1))
        # print(s1)
        if len(s1) != len(l1):
            return False

        s1.sort()
        if s1 == l1:
            return True

        return False
