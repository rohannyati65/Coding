# 2032. Two Out of Three (leetcode)
class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        l = []
        l = l + nums1 + nums2 + nums3
        s = list(set(l))
        s1 = list(s)
        for i in s:
            c = 0
            if i in nums1:
                c += 1

            if i in nums2:
                c += 1

            if i in nums3:
                c += 1

            if c < 2:
                s1.remove(i)
        return s1
