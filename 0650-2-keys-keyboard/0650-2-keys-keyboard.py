class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0
        
        memo = defaultdict()
        def dp(num, size_of_copy):
            if num > n:
                return float('inf')
            if num == n:
                return 0
            if (num, size_of_copy) not in memo:
                with_copy = 2 + dp(2 * num, num)
                if num == 1:
                    with_copy -= 1
                without = 1 + dp(num + size_of_copy, size_of_copy)                
                memo[(num, size_of_copy)] = min(with_copy, without)
            
            return memo[(num, size_of_copy)]
        
        return dp(1, 1) + 1