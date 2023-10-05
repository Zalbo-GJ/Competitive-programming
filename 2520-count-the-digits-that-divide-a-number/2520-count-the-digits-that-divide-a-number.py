class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        digits = list(map(int, str(num)))
        
        for dig in digits:
            if num % dig == 0:
                ans += 1
        
        return ans
        