class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        que = deque([[entrance[0],entrance[1], 0]])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set(entrance)
        def validate(r,c):
            if  not ( 0 <= r < len(maze) and 0 <= c < len(maze[0])) or maze[r][c] == "+" :
                return False
            
            return True
        
        while que:
            
            row, col, steps = que.popleft()
            
            if (row == 0 or  col == 0 or row == len(maze)-1 or col == len(maze[0])-1 ) and [row,col] != entrance:
                return steps
            
            for r,c in directions:
                dr, dc = row + r, col + c
                
                if validate(dr,dc) and (dr,dc) not in visited:
                    visited.add((dr,dc))
                    que.append([dr,dc, steps + 1])
        
        return -1
            
            
            