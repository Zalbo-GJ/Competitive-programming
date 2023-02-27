class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        1. we expand and add the chars in dict
        2. if char exist in dict then compress untill 
        """
        
        dic = {}
        l = 0
        maxx = 0
        
        for r in range(len(s)):
        
            while s[r] in dic:
                
                del(dic[s[l]])
                l += 1
    
            dic[s[r]] = 1
            
            maxx = max(maxx, r-l+1)
        
        return maxx