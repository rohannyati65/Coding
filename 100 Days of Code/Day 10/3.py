# 35. Search Insert Position (leetcode)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            x = nums.index(target)
            return x
        else:
            nums.append(target)
            nums.sort()
            x = nums.index(target)
            return x
