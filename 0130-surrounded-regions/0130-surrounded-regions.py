class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def inBound(r,c):
            return 0 <= r < m  and 0 <= c < n 
    
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            if not inBound(r,c):
                return False
            if board[r][c] == "X" or (r,c) in visited:
                return True
            
            flag = True
            segment.append([r,c])
            visited.add((r, c))
            
            for dr, dc in directions:
                flag = dfs(r + dr, c + dc) and flag
            
            return flag
        
        visited = set()
        segment = []
        for r in range(m):
            for c in range(n):
                
                if board[r][c] == "O" and (r,c) not in visited:
                    flag = dfs(r,c)
                    if flag:
                        for i, j in segment:
                            board[i][j] = "X"
                        
                    segment = []
                    