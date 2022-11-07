class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        l = 0
        ans = float('inf')
        seen = set()
        
        for r in range(len(cards)):
            
            while cards[r] in seen:
                ans = min(ans , r-l+1)
                seen.remove(cards[l])
                l+=1
            seen.add(cards[r])
            
        return ans if ans<=len(cards) else -1
            
            
            