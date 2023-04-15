class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def magical(a,b,c,d,e,f,g,h,i):
            sor = sorted([a,b,c,d,e,f,g,h,i])
            rng = list(range(1,10))
            is_equal = (a+b+c == d+e+f == g+h+i ==a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15 )          
            
            return sor == rng and is_equal
            
        ans = 0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                
                 if magical(grid[r][c], grid[r][c+1], grid[r][c+2], grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2], grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
                        
                        
            
        return ans
        
