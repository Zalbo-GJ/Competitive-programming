class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        digs = list(map(int, str(n)))
        add = True
        ans = 0
        for d in digs:
            if add:
                ans += int(d)
            else:
                ans -= int(d)
            
            add = not add
        
        return ans
        