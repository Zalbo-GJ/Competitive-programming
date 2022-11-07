class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        l = 0
        r = 1
        ans = 0
        seen = set(word[0])
        
        while r<len(word) and len(word)>1 :
            
            if word[r]< word[r-1]:
                seen.clear()
                l = r
            seen.add(word[r])
            if len(seen)== 5:
                ans = max(ans, r-l+1)
                
            r+=1
        return ans
            
            
            
            
            
            