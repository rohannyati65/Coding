# 540. Single Element in a Sorted Array (leetcode)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
