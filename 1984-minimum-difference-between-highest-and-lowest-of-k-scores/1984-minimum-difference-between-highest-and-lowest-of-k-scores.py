class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        
        l = 0
        r = 0
        ans = float('inf')
        
        while r< len(nums):
            if r-l+1 < k:
                r+=1
            else:
                ans = min(ans,nums[r]-nums[l])
                
                l+=1
                r+=1
        return ans