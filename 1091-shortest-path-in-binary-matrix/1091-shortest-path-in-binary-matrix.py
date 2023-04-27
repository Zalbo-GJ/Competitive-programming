class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
        
        def validation(r,c):
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0]))  and grid[r][c] == 0:
                return True
            else:
                return False
            
        visited = set()
        que = deque([[0,0,1]])
        directions = [[1,1],[1,-1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,0]]
        
        while que:
            row, col, level = que.popleft()
            
            for dr, dc in directions:
                newR, newC = row + dr, col + dc
                
                
                if validation(newR, newC):
                    if newR == newC == len(grid)-1 :
                        return level + 1

                    if (newR, newC) not in visited :
                        visited.add((newR, newC))
                        que.append([newR, newC, level + 1])
        
        return -1
                    
            
        
        
        
        