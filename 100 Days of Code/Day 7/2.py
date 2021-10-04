# 463. Island Perimeter (leetcode)


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    p = p + 4
                    if i > 0 and (grid[i - 1][j] == 1):
                        p = p - 2

                    if j > 0 and (grid[i][j - 1] == 1):
                        p = p - 2
        return p
