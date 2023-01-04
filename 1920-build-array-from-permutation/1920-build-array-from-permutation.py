class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for i in nums:
            ans.append(nums[i])
        
        return ans