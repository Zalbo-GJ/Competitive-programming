class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l ,r = 0, 0
        
        while r < len(prices):
            ans = max(ans, prices[r] - prices[l])
            if r + 1 < len(prices) and prices[r + 1] > prices[l]:
                r += 1
            else:
                r += 1
                l = r
        return ans
        
        