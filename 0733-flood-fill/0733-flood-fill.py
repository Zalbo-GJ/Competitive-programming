class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(row, col):
            
            if row >= len(image) or col >= len(image[0]) or \
            row < 0 or col < 0 or image[row][col] != scolor:
                
                return
            
            image[row][col] = color
            
            for move in moves:
                
                dfs(row + move[0], col + move[1])
        
        moves = [[-1,0],[0,1],[1,0],[0,-1]]
        scolor = image[sr][sc]
        if scolor == color:
            return image
        dfs(sr, sc)
        
        return image
                
            
            