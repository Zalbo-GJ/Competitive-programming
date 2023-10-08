class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s = list(str(num))
        
        for idx in range(len(s)):
            if s[idx] == "6":
                s[idx] = "9"
                
                return int("".join(s))
        
        return num