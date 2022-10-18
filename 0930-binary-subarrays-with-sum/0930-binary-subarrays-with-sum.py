class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        presum = 0
        count = defaultdict(int)
        count[0]=1
        ans = 0
        for i in nums:
            presum += i
            if presum-goal in count:
                ans+=count[presum-goal]
            
            count[presum] += 1
                
        return ans
       