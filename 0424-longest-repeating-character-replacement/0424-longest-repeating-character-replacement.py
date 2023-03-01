class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        ans = 0
        d = {}
        while r < len(s):
          
            if s[r] in d:
                d[s[r]] += 1    
            else:
                d[s[r]] = 1

            while d and self.minSwap(d,r-l+1) > k:
                
                d[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
            
            r += 1
            
        return ans
    
    
    def minSwap(self,d,winSize):
        
        m = max(d.values())
        
        return winSize - m