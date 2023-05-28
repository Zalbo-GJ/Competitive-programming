class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        def dp(n):
            
            if n not in memo:
                if n <= 1:
                    memo[n] = n
                    return memo[n]
                if n % 2 == 0:
                    memo[n] = dp(n // 2)
                else:
                    memo[n] = dp(n // 2) + dp((n // 2) + 1)
            
            return memo[n]
        
        for idx in range(n + 1):
            dp(idx)
        
        return max(memo.values())