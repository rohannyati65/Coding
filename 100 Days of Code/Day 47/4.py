# 448. Find All Numbers Disappeared in an Array (leetcode)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        if len(nums) == len(set1):
            x = max(nums)
            lst = []
            for i in range(1, x):
                lst.append(i)
            set2 = set(lst)
            set3 = set2.difference(set1)
            lst1 = list(set3)
            return lst1
        else:
            z = len(nums)
            lst = []
            for i in range(1, z + 1):
                lst.append(i)
            set2 = set(lst)
            set3 = set2.difference(set1)
            lst1 = list(set3)
            return lst1
