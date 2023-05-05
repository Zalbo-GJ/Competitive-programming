class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def outOfBound(r, c):
            return r < 0 or c < 0 or r == n or c == n       
        
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r, c):
            if  outOfBound(r,c) or not grid[r][c] or (r,c) in visited:
                return
            
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            que = deque(visited)
            ans = 0
            while que:
                for _ in range(len(que)):
                    
                    r, c = que.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if  outOfBound(curR, curC) or (curR, curC) in visited:
                            continue
                        if grid[curR][curC]:
                            return ans
                        que.append([curR, curC])
                        visited.add((curR, curC))
                
                ans += 1
            
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
        
        
        
            
            