# 5898. Kth Distinct String in an Array (leetcode)
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = 0
        for i in arr:
            if arr.count(i) == 1:
                a += 1
                # print(i,a)
                if a == k:
                    return i
        return ""
