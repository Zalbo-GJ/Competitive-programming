class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        while n > 0:
            
            digs = list(map(int, str(n)))
            
            n = 0
            for i in digs:
                n += i ** 2
                
            if n == 1:
                return True
            
            if n in visited:
                return False
            else:
                visited.add(n)
            
        
        return False