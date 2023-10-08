class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        ans = 0
        
        r1, c1 = 0, 0
        r2, c2 = 0, len(mat) - 1
        
        while r1 < len(mat) and c1 < len(mat) :
            
            ans += mat[r1][c1]
            
            if c1 != c2:
                
                ans += mat[r2][c2]
            
            r1 += 1
            c1 += 1
            r2 += 1
            c2 -= 1
        
        return ans