class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        m = (10**9 )+7
        
        maxx = (2**p)-1
        return maxx*( pow((maxx-1),((maxx-1)/2),m))%m