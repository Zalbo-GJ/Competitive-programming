class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} 
        def climb(n):
            if n == 0 or n - 1 == 0:
                return 1
            if n not in memo:
                one = climb(n - 1)
                two = climb(n - 2)
                memo[n] = one + two
            
            return memo[n]
        
        return climb(n)