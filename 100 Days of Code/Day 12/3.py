# 283. Move Zeroes (leetcode)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums.remove(0)
                    nums.append(0)
