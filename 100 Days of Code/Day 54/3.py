# 2089. Find Target Indices After Sorting Array (leetcode)
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = []
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        return l
