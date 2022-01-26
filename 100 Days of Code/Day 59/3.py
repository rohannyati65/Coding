# Two Sum (leetcode)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (
                (nums[i] - target in nums)
                and (i != nums.index(nums[i] - target))
                and (nums[i] + nums[nums.index(nums[i] - target)] == target)
            ):
                return [i, nums.index(nums[i] - target)]

            elif (
                (target - nums[i]) in nums
                and (i != nums.index(target - nums[i]))
                and (nums[i] + nums[nums.index(target - nums[i])] == target)
            ):
                return [i, nums.index(target - nums[i])]
