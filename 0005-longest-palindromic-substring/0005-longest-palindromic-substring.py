class Solution:
    def longestPalindrome(self, s: str) -> str:
        
      
        i = 0
        longest = s[i]
        while i < len(s):
            j = i+1
            while j <= len(s):
                arr = s[i:j]
                if arr == arr[::-1] and j-i > len(longest):
                    longest = arr
                j += 1
            
            i += 1
        
        return "".join(longest)
        