# 476. Number Complement (leetcode)
class Solution:
    def findComplement(self, num: int) -> int:
        s = str(bin(num).replace("0b", ""))
        # print(s)
        a = ""
        for i in range(len(s)):
            if s[i] == "0":
                a = a + "1"

            elif s[i] == "1":
                a = a + "0"
            # print(a)

        return int(a, 2)
