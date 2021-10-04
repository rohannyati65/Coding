# 55. Jump Game (leetcode)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f=0
        
        for i,v in enumerate(nums):
            if(i>f):
                return(0)
            f=max(i+v,f)
        return(1)
        
        
        