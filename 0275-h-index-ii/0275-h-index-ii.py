class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l= 0
        r = len(citations) - 1
        maxx = 0
        while l <= r:
            
            mid = (l + r) // 2
            
            if len(citations) - mid <= citations[mid]:
                r-=1
                maxx = max(len(citations) - mid, maxx)
            else:
                l+= 1
                
        return maxx