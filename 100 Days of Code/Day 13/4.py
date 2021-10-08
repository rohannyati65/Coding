# 344. Reverse String (leetcode)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        # if len(s)==1:
        #    return(s)
        # else:
        #    s=self.reverseString(s[1:])+list(s[0])
