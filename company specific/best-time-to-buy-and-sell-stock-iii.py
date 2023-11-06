class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(maxsize = None)
        def dp(idx, canBuy, totalBought):
            if totalBought > 2 or idx == len(prices):
                return 0
            
            sold = 0
            bought = 0
            if canBuy:
                bought = dp(idx + 1, False, totalBought + 1, ) - prices[idx]
            
            else:
                sold =  dp(idx + 1, True, totalBought) + (prices[idx])
                
            jump = dp(idx + 1, canBuy, totalBought)

            return max(jump, sold, bought)
        
        return dp(0, True, 0)
            
            