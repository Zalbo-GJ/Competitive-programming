class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        l = 0
        r = len(s) - 1
        s = list(s)
        
        while l < r:
            if s[l] != s[r]:
                if s[l] < s[r]:
                    s[r] = s[l]
                else:
                    s[l] = s[r]
            
            l += 1
            r -= 1
        
        return "".join(s)
                