# 41. First Missing Positive  (leetcode)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        a = 1
        for i in nums:
            if i > 0:
                if i == a:
                    a = a + 1
                else:
                    return a
        if nums[-1] < 1:
            return 1
        else:
            return nums[-1] + 1
