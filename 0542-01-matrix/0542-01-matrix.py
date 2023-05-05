class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0 for _ in range(n)]for _ in range(m)] 
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()       
        que = deque()
        
        def outOfBound(r, c):
            return r < 0 or c < 0 or r == m or c == n
        
        def bfs(que):
            while que:
                r, c, length = que.popleft()
                
                for dr, dc in directions:
                    curR, curC = r + dr, c + dc
                    
                    if not outOfBound(curR, curC) and (curR, curC) not in visited and mat[curR][curC]:
                        ans[curR][curC] = length + 1
                        que.append([curR, curC, length + 1])
                        visited.add((curR, curC))
                        
        for r in range(m):
            for c in range(n):
                if not mat[r][c]:
                    que.append([r,c,0])
        
        bfs(que)
                    
        return ans
                    