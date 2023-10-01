class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for idx in range(1, len(s), 2):
            shift = int(s[idx])
            s[idx] = chr(ord(s[idx - 1]) + shift)
        
        return "".join(s)