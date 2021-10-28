# 231. Power of Two (leetcode)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n>=1):
            if(n==1):
                return(True)
            n=n/2
        return(False)