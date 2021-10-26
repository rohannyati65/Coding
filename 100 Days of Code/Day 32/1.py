# 628. Maximum Product of Three Numbers (leetcode)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[-1] * nums[-2] * nums[-3]
        y = nums[-1] * nums[0] * nums[1]
        return max(x, y)
