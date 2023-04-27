class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
        
        visited = set()
        que = deque([[0,0,1]])
        moves = [[1,1],[1,-1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,0]]
        
        while que:
            row, col, level = que.popleft()
            
            for dr, dc in moves:
                newR, newC = row + dr, col + dc
                
                if (0 <= newR < len(grid)) and (0 <= newC < len(grid[0])):

                    if newR == newC == len(grid)-1  and grid[newR][newC] == 0:
                        return level + 1

                    if (newR, newC) not in visited and grid[newR][newC] == 0:
                        visited.add((newR, newC))
                        que.append([newR, newC, level + 1])
        
        return -1
                    
            
        
        
        
        