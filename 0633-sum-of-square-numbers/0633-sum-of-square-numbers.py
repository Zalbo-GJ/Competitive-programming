class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        root = int(c**0.5)
        
        l = 0
        r = root
        
        while l <= r:
            
            res = l**2 + r**2 
            
            if res == c:
                return True
            elif res < c:
                l += 1
            else:
                r -= 1
                
                
        return False
            