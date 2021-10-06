# 189. Rotate Array (leetcode)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        x=len(nums)
        #print(27//5)
        if(k==x):
            return
        elif(k>x):
            y=(k//x)
            k=k-(x*y)
            #print(k)
            z=nums[-k:]
            #print(z)
            nums[:]=z+nums[:-k]
            #print(nums)
            return
        elif(k<x):
            z=nums[-k:]
            #print(z)
            nums[:]=z+nums[:-k]
            #print(nums)
            return