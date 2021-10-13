# 2027. Minimum Moves to Convert String (leetcode)
class Solution:
    def minimumMoves(self, s: str) -> int:
        f = 0
        l = len(s) - 1
        c = 0
        while f <= l:
            if s[f] == "X":
                c += 1
                f = f + 3
            else:
                f = f + 1
        return c

        """
        if 'X' in s:
            a=len(s)
            if(a%3==0):
                return(a//3)
            else:
                return((a//3)+1)
            
        return(0)
        """
