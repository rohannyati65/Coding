# 15. 3Sum (leetcode)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                if a + b + c == 0:
                    if [a, b, c] not in l:
                        l.append([a, b, c])
                    start += 1
                    end -= 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    start += 1
        return l

        # if(len(nums)<3):
        #    return([])
        # else:
        #   l=list(map(list,itertools.combinations(nums,3)))
        #    l1=[list(i) for i in l if(sum(i)==0)]
        #    print(l1)
        #    l2=[]
        ##    if(len(l1)>0):
        #       for i in range(len(l1)-1):
        #            a=list(l1[i])
        #            a.sort()
        #            for j in l1[i+1:]:
        #                b=list(j)
        #                b.sort()
        #                if(a==b):
        #                    #l1.remove(l1[i])
        #                    l2.append(i)
        #       for i in l2:
        #           l1.remove(l1[i])
        #
        #  return(l1)
