# Sort Array By Parity II  (leetcode)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e = []
        o = []
        for i in nums:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)

        e.sort()
        o.sort()
        x = len(e)
        l = []
        for i in range(len(nums) // 2):
            if (len(e) - 1) >= i:
                l.append(e[i])

            if (len(o) - 1) >= i:
                l.append(o[i])

        return l
