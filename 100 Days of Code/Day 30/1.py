# 1752. Check if Array Is Sorted and Rotated (leetcode)
class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        x = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                x = i + 1

        a = nums[x:] + nums[:x]
        nums.sort()
        if nums == a:
            return True
        return False
