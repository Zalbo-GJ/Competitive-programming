class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zCount = ans = l= r=0
        
        while r<len(nums):
            
            if nums[r]==0:
                zCount += 1
            while zCount > 1:
                if nums[l]==0:
                    zCount-=1
                l+=1
            
            ans = max(ans, r-l)
            r+=1
        return ans