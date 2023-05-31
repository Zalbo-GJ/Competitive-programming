class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def dp(i,j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) not in memo:
                right = dp(i, j + 1)
                down = dp(i + 1, j)
                memo[(i, j)] = right + down
            
            return memo[(i, j)]
        
        return dp(0, 0)