class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        ans = 0
        for i in range(1, min(a, b) + 1):
            if not a % i and not b % i:
                ans += 1
        
        return ans