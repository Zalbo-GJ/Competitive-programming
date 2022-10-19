class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        l = ans = 0
        
        for r in range(len(s)):
            
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1
            
            if r-l+1 >= 3:
                if len(d) == 3:
                    ans += 1
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                
                l+=1
                
        return ans