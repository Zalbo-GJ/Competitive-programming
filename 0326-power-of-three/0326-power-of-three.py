class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n<1:
            return False
        return n%3==0 and self.isPowerOfThree(n/3)