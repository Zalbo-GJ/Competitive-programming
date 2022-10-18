class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum = sum(nums)
        
        left = 0
        
        for i, num in enumerate(nums):
            
            if presum - left-num == left:
                return i
            left+=num
        return -1