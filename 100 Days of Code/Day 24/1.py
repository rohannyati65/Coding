# 496. Next Greater Element I (leetcode)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            x=nums2.index(nums1[i])
            if(x==(len(nums2)-1)):
                nums1[i]=-1
            else: 
                for j in range(x+1,len(nums2)):
                    a=0
                    if(nums2[j]>nums1[i]):
                        a=1
                        nums1[i]=nums2[j]
                        break
                if(a==0):
                    nums1[i]=-1
        return(nums1)
            