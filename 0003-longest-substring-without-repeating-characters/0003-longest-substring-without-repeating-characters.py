class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        ans = 0
        l = 0
        
        for r, char in enumerate(s):
            if char in d and l <= d[char]:
                l = d[char]+1
                
            else:
                ans = max(ans, r-l+1)
            d[char] = r
            
        return ans