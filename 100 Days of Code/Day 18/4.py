# 695. Max Area of Island (leetcode)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if (
                                0 <= nr < len(grid)
                                and 0 <= nc < len(grid[0])
                                and grid[nr][nc]
                                and (nr, nc) not in seen
                            ):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
        """
        l=[0]
        R=len(grid)
        C=len(grid[0])
        def dfs(r,c):
            if((r<0) or (r>=len(grid)) or (c<0) or (c>=len(grid[0])) or (grid[r][c]!=1)):
                return(0)
            
            if(grid[r][c]==1):
                grid[r][c]=2
                count=1
                if r>=1:
                    #print(count)
                    count+=dfs(r-1,c) 
                    #return(x)
                
                if r+1<R: 
                    #print(count)
                    count+=dfs(r+1,c)
                    #return(x)
                    
                if c>=1: 
                    #print(count)
                    count+=dfs(r,c+1)
                    #return(x)
                    
                if c+1<C: 
                    #print(count)
                    count+=dfs(r,c-1)
                    #return(count)
                    
            #print(count) 
            #count=count
                return(count)    
        
            
        for i in range(R):
            for j in range(C):
                if(grid[i][j]==1):
                    x=dfs(i,j)
                    l.append(x)
        #print(l)
        return(max(l))
        """
