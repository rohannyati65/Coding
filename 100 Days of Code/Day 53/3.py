# 238. Product of Array Except Self (leetcode)
import numpy


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        pref_product = 1
        for i in range(len(nums) - 1):
            pref_product = pref_product * nums[i]
            l.append(pref_product)

        l1 = [1]
        suf_product = 1
        nums = nums[::-1]
        for i in range(len(nums)):
            suf_product = suf_product * nums[i]
            l1.append(suf_product)
        # l1.insert(0,1)
        l1 = l1[:-1]
        l1 = l1[::-1]
        # print(l,l1)
        ans = []
        for i in range(len(l)):
            ans.append(l[i] * l1[i])

        return ans
