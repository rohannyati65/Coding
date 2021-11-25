# 53. Maximum Subarray (leetcode)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_tn = -12345
        max_e = 0

        for i in nums:
            max_e = max_e + i

            max_tn = max(max_tn, max_e)

            if max_e < 0:
                max_e = 0
        return max_tn
