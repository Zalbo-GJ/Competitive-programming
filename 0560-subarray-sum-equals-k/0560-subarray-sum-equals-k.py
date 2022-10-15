class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        psum = 0
        d = {0:1}
        ans = 0
        for i in nums:
            psum += i
            
            if psum-k in d:
                ans += d[psum-k]
            if psum not in d:
                d[psum] = 1
            else:
                d[psum] += 1
        return ans