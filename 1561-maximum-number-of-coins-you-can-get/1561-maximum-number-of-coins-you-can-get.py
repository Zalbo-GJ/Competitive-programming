class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse = True)
        
        i = 0
        j = 1
        ans = 0
        while i < len(piles)//3:
            
            ans += piles[j]
            j+=2
            i+=1
        
        return ans
            
            
            