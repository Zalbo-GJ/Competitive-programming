class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        if b in a:
            return 1
        for i in range(0, (len(b) // len(a))+ 3):
            if b in i * a:
                return i
        
        return -1