class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        presum = [0]
        ans = 0
        
        for i in gain:
            presum.append(presum[-1]+i)
        
        return max(presum)