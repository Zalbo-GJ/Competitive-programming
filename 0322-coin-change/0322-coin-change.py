class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(lambda : float('inf'))
        def dp( summ ):
            
            if summ > amount:
                return float('inf')
            if summ == amount:
                return 0
            
            if summ not in memo:
                for coin in coins:
                    res = dp(summ + coin) + 1
                    memo[summ] = min(res,memo[summ])
            
            return memo[summ]
    
        ans = dp(0)
        
        return ans if ans != float('inf') else -1
        

        