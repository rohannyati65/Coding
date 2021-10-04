# 169. Majority Element (leetcode)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=list(set(nums))
        a=len(nums)//2
        for i in s:
            if((nums.count(i))>a):
                return(i)
