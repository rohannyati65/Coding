# 215. Kth Largest Element in an Array (leetcode)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
