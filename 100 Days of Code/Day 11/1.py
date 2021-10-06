# 442. Find All Duplicates in an Array (leetcode)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        f=[0]*(len(nums)+1)
        l=[]
        for i in nums:
            if(f[i]==1):
                l.append(i)
                
            else:
                f[i]=1
        return(l)
        
        
