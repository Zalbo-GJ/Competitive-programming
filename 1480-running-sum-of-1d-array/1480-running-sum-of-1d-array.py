class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        presum = 0
        
        for i in nums:
            presum += i
            ans.append(presum)
        
        return ans
        