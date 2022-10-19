class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """ 
        ans = avr = sum(nums[:k])
        
        for r in range(k, len(nums)):
            
            avr += nums[r]-nums[r-k]
            
            ans = max(ans, avr)
            
            
        return ans/float(k)