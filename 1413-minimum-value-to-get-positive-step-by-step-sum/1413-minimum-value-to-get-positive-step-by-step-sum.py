class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum = 0
        low = float('inf')
        for i in nums:
            presum += i
            low = min(low,presum)
        
        return abs(low) + 1 if low < 1 else 1