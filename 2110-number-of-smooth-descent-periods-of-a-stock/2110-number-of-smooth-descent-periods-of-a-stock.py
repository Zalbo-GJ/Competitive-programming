class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = ans = 1
        
        for i in range(1,len(prices)):
            if prices[i-1]-prices[i] == 1:
                count += 1
            else:
                count = 1
            ans += count
        return ans