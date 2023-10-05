class Solution:
    def addDigits(self, num: int) -> int:
        
        
        while num > 0:
            
            digs = list(map(int, str(num)))
            if len(digs) == 1:
                return digs[0]
            num = 0
            for i in digs:
                num += i
            
        return 0
            
        