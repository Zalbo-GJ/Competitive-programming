class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        ans = 0
        l = summ = 0
        
        for r in nums:
            
            while r in seen:
                summ -= nums[l]
                seen.remove(nums[l])
                l+=1
            
            summ+= r
            seen.add(r)
            
            ans = max(ans, summ)
        return ans