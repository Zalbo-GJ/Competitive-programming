class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        r = len(p)
        pCount = Counter(p)
        ans = []
        while r <= len(s):
            
            sCount = Counter(s[r-len(p):r])
            
            if sCount == pCount:
                ans.append(r-len(p))
            
            r += 1
                
        
        return ans
                
      