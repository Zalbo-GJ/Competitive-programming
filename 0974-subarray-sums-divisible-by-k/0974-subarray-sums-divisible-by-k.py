class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        presum = ans = 0
        for i in range(len(nums)):
            presum += nums[i]
            rem = presum%k
            if rem in d:
                ans+=d[rem]
                d[rem]+=1
                
            else:
                d[rem] = 1
        return ans
            