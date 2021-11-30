# 240. Search a 2D Matrix II (leetcode)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return(True)
        return(False)
        