class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        
        while n > 1:
            
            if n % 2 == 0:
                n /= 2
                ans += n 
            else:
                ans += (n - 1) / 2 + 1
                n = (n - 1) / 2
        
        return int(ans)