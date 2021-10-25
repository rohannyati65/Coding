# 1365. How Many Numbers Are Smaller Than the Current Number (leetcode)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return [0]
        l = []
        lst = list(nums)
        lst.sort()
        for i in nums:
            a = lst.index(i)
            l.append(a)
        return l
