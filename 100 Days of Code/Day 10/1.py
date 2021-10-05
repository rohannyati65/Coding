# 704. Binary Search (leetcode)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        found = False
        while first <= last and not found:
            mid = (first + last) // 2
            if nums[mid] == target:
                found = True
            else:
                if target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        if found == True:
            return mid
        if found == False:
            return -1
