# 75. Sort Colors (leetcode)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l1=[]
        l2=[]
        l3=[]
        for i in nums:
            if(i==0):
                l1.append(i)
            if(i==1):
                l2.append(i)
            if(i==2):
                l3.append(i)
        nums[:]=l1+l2+l3
        """
        Do not return anything, modify nums in-place instead.
        """
        