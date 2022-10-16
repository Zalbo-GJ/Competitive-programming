class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        presum = sum(chalk)
        k = k%presum
        
        if len(chalk) == 1:
            return 0
        
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k-= chalk[i]