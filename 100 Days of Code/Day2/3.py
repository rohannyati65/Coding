# Sort Array by Increasing Frequency (leetcode)

import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c1 = collections.Counter(nums)
        nums.sort(key=lambda x: (c1[x], -x))
        return nums
