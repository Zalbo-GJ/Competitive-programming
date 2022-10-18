class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum = ans = 0
        d = {0:-1}
        
        for i in range(len(nums)):
            presum += 1 if nums[i] else -1
            
            # if presum == 0:
            #     ans+=1
            if presum in d:
                ans = max(ans, i-d[presum])
            else:
                d[presum] = i
                
        return ans
        
        