class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        idx = 0
        ans = 0
        
        while idx < len(s):
            
            zero_count = 0
            one_count = 0
            
            while idx < len(s) and s[idx] == "0":
                zero_count += 1
                idx += 1
            while idx < len(s) and s[idx] == "1":
                one_count  += 1
                idx += 1
            
            ans = max(ans, 2 * min(zero_count, one_count))
        
        return ans