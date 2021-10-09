# 912. Sort an Array (leetcode)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
        """
        n=len(nums)
        maxelement=max(nums)
        l=[]
        buckets=[l]*10
        for i in range(n):
            j=int((nums[i]*n)/(maxelement+1))
            if(len(buckets[j])==0):
                buckets[j]=[nums[i]]
            else:
                buckets[j].append(nums[i])
                
        for i in range(10):
            n=len(buckets[i])
            for j in range(1,n):
                cvalue=buckets[i][j]
                position=j
                while((position>0) and (buckets[i][position-1]>cvalue)):
                    buckets[i][position]=buckets[i][position-1]
                    position=position-1
                buckets[i][position]=cvalue
            
        k=0
        for i in range(10):
            for j in range(len(buckets[i])):
                nums[i]=buckets[i].pop(0)
                k=k+1
                
        return(nums)
        """
