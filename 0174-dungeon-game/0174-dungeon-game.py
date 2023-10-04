class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        dp[n][m - 1], dp[n - 1][m] = 1, 1
        
        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                
                dp[row][col] = max( min(dp[row][col + 1], dp[row + 1][col]) - dungeon[row][col], 1)
        
        return dp[0][0]
                