class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder = {0:-1}
        tot = 0
        
        for i, num in enumerate(nums):
            tot += num
            rem = tot%k
            
            if rem not in remainder:
                remainder[rem] = i
            elif i - remainder[rem] >1:
                return True
        return False