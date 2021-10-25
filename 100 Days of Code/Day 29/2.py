# 1800. Maximum Ascending Subarray Sum (leetcode)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        s = 0
        x = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                x = x + nums[i]
                s = max([s, x])
            else:
                s = max([s, x])
                x = nums[i]

        return s
