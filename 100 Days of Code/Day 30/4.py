# 1437. Check If All 1's Are at Least Length K Places Away (leetcode)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True

        x = nums.index(1)
        for i in range(x + 1, len(nums)):
            if nums[i] == 1:
                # print(i,x)
                y = i - x - 1
                # print(y)
                if y >= k:
                    x = i
                else:
                    return False
        return True
