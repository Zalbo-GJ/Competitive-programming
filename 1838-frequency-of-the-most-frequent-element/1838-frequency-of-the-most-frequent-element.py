class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = r = tot = window = 0
        nums.sort()
        while r< len(nums):
            tot += nums[r]
            
            while nums[r]* (r-l+1) > tot + k:
                tot-= nums[l]
                l+=1
            window = max(window , r-l+1)
            r+=1
        return window