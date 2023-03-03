class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        
        while l <= r:
            mid = l + (r-l) // 2
            
            if self.countDays(weights,mid) > days:
                l = mid + 1
            else:
                r = mid-1
        return l        
    
    
    def countDays(self, w, limit):
        
        i = 0
        count = 0
        
        while i < len(w):
            summ = 0
            while i <len(w) and summ + w[i] <= limit:
                summ += w[i]
                i += 1
            
            count += 1
        
        return count
        
        
        
        