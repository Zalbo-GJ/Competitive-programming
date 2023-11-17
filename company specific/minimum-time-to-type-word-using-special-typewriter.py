class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 1
        ans = 0
        
        for char in word:
            idx = ord(char) - ord('a') + 1
            
            ans += min( (26 - curr + idx ) % 26,  (26 - idx + curr) % 26 )
            curr = idx
        
        return ans + len(word) 