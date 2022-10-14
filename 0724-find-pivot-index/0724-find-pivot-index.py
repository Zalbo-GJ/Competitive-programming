class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = sum(nums)
        left = 0
        
        for i,num in enumerate(nums):
            if left == (tot-left-num):
                return i
            left+=num
            
        return -1