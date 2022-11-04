class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        
        l = 0
        r = 0
        ans = 0
        latest_mn = -1
        latest_mx = -1
        
        for r in range(len(nums)):
            
            if nums[r] > maxK or nums[r] < minK:
                latest_mn = -1
                latest_mx = -1
                l=r+1
            if nums[r] == minK:
                latest_mn = r
            if nums[r] == maxK:
                latest_mx = r
            if latest_mn != -1 and latest_mx != -1:
            
                ans += min(latest_mn,latest_mx)-l + 1
        
            
            
        return ans
            
            