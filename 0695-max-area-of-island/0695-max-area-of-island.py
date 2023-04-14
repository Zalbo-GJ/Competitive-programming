class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(area, row, col):
            
            if row >= len(grid) or col >= len(grid[0]) or \
            tuple([row, col]) in visited or grid[row][col] == 0 \
            or row < 0 or col < 0:
                
                return area
            
            visited.add(tuple([row, col]))
            area += 1
            for move in moves:
                
                area = dfs(area, row + move[0], col + move[1])
                
            return area
        
        
        moves= [[-1,0],[0,1],[1,0],[0,-1]]
        visited = set() 
        mxarea = 0  
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    area = dfs(0, row, col)
                    mxarea = max(mxarea, area)
                    
        return mxarea
                