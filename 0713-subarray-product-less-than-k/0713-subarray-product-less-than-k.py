class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pro = 1
        ans = l = 0
        
        if k<=1: return 0
        
        for r, val in enumerate(nums):
            pro *= val
            
            while pro >= k:
                pro /= nums[l]
                l += 1
                
            ans += r-l+1
            
        return ans
    