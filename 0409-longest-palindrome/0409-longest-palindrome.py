class Solution:
    def longestPalindrome(self, s: str) -> int:
        sett = set()
        
        for char in s:
            if char in sett:
                sett.remove(char)
            else:
                sett.add(char)
        
        return len(s) - len(sett) + 1 if len(sett) else len(s)