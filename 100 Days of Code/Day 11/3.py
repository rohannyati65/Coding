# 977. Squares of a Sorted Array (leetcode)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # lst=[]
        for i in range(len(nums)):
            a = nums[i]
            nums[i] = a * a
            # print(nums[i])
        nums.sort()
        # print(nums)
        return nums
