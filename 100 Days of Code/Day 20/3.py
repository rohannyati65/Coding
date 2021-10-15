# 77. Combinations (leetcode)
import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[i for i in range(1,n+1)]
        l1=list(map(list,itertools.combinations(l,k)))
        return(l1)
    
    