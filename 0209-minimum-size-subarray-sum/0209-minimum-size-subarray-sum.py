class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l  = tot = 0
        ans = len(nums)+1
        for r in range(len(nums)):
            tot += nums[r]
            
            while tot>=target:
                ans = min(ans, r-l+1)
                tot -= nums[l]
                l+=1
        return ans if ans <= len(nums) else 0
            