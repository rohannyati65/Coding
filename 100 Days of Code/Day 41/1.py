# 541. Reverse String II (leetcode)

# Here we divide the string into groups of 2*k , for that we first find
# the no of groups we will get and add 1 to get the last case when len of
# s is less than 2*k . After that for every 2*k len of string we keep
# reversing the first k values .


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        x = (len(s) // (2 * k)) + 1
        a = 0
        while x != 0:
            x = x - 1
            y = s[a : a + k]
            # y=y[::-1]
            s = s.replace(y, y[::-1])
            # s=str(y+s[a+k:])
            a = a + 2 * k
            # print(y,s,a)
        return s
