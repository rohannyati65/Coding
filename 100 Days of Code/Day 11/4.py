# 268. Missing Number (leetcode)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=0
        if a not in nums:
            return(a)
        
        for i in range(len(nums)):
            a=a+1
            if a not in nums:
                return(a)
        