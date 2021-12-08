# 56. Merge Intervals (leetcode)
#Here in this Solution we compare each index list with its neighbouring list , and check whether the first value lie in the range of its precceding index values and if it lies we create a new list with those 4 values of the given index and succeding index values and create a new list and add this in the intervals list and remove the current index value and succeding index value fromn the list .
#If their is no similarity between the current index values and succeding index values then we increase the index value by 1 , and keep on increasing till the last index value of the intervals list .
#For better understanding remove the "#" commenting symbol from the code and run it once .
```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        while(i!=len(intervals)-1):
            if (intervals[i+1][0]) in range(intervals[i][0],intervals[i][1]+1):
                x=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i+1][1],intervals[i][1])]
                intervals.pop(i+1)
                intervals.pop(i)
                intervals.insert(i,x)
            
            else:
                i+=1
			#print(i,intervals)
        return(intervals)
```
#If u understood the code then plz......UPVOTE......thnx in adv