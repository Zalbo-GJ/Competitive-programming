class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        if n == 0: return 0
        if n == 1: return 1
        
        if n-1 not in memo:
            memo[n-1]= self.fib(n-1)
        if n-2 not in memo:
            memo[n-2]= self.fib(n-2)
        return memo[n-1]+memo[n-2]