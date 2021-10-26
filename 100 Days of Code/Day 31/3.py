# 326. Power of Three (leetcode)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #if(n==1):
        #    return(False)
        
        while(n>=1):
            if(n==1):
                return(True)
            n=n/3
        return(False)
            
            