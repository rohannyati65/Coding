# 209. Minimum Size Subarray Sum (leetcode)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        s=0
        res=len(nums)+1
        while(r<len(nums)):
            s=s+nums[r]
            while(s>=target):
                res=min([res,r-l+1])
                s=s-nums[l]
                l=l+1
            r=r+1
        return res if res<=len(nums) else 0
            
            
            
            
        
        