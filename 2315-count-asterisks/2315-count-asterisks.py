class Solution:
    def countAsterisks(self, s: str) -> int:
        brace_open = False
        ans = 0
        for ch in s:
            if ch == "|":
                brace_open = not brace_open
            
            if ch == "*" and not brace_open:
                ans += 1
        
        return ans