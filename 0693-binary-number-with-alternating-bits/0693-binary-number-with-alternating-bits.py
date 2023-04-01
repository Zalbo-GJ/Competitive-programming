class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        prev = n & 1
        while n > 0:
            n >>= 1
            if n & 1 == prev:
                return False
            
            prev = n & 1
        
        return True
            
        