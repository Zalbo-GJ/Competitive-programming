class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        part_count = 0
        
        def recur( start , end , prev):
            nonlocal part_count
            if start == n and part_count > 1:
                return True
            
            if end == n:
                return False
            
            res1 = False
            if prev == None or prev - 1 == int(s[start:end+1]):
                part_count += 1
                res1 = recur(end+1, end+1,int(s[start:end+1]) )
                part_count -= 1
            
            res2 = recur(start, end+1 , prev)
        
            return res1 or res2
        
        return recur(0, 0, None)
        
        
    
        
        