class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
 
        def dfs(row, col):
            if not 0 <= row < m or not 0 <= col < n or not grid2[row][col] \
            or tuple([row,col]) in visited:
            
                return True
            
            visited.add(tuple([row, col]))
            ret = True
            
            if grid1[row][col] == 0:
                ret = False
            
            ret = dfs(row + 1, col) and ret
            ret = dfs(row - 1, col) and ret
            ret = dfs(row , col+1) and ret
            ret = dfs(row , col -1) and ret
                
            return ret
        
        ans = 0
        visited = set()
        m = len(grid1)
        n = len(grid1[0])
        
        for i in range(m):
            for j in range(n):
                
                if grid2[i][j] and tuple([i, j]) not in visited and  dfs(i,j):
                    ans += 1
        
        return ans
        
        