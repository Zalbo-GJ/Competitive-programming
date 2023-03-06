class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
    
        l = 1
        r = max(piles)
        mini = max(piles)

        while l <= r:
            
            mid = (l + r) // 2
            
            time = self.howLong(piles, mid)

            if time <= h:
                mini = min(mid,mini)
                r = mid -1
            else:
                l = mid + 1
             
        return mini
                
    
    
    def howLong(self, p, k):
        hours = 0
        for i in p:
            
            hours += ceil(i/k)
            
        return hours
        
        
        