class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = float('inf')
        ans = 0
        
        for price in prices:
            if buy > price:
                buy = price
                continue
            
            ans = max(price - buy, ans)
        
        return ans