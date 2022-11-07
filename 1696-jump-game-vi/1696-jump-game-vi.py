class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dq = deque([(nums[0], 0)])
        
        for i in range(1,len(nums)):
            while dq and dq[0][1] +k < i:
                dq.popleft()
            cost = nums[i]+ dq[0][0]
            while dq and cost >= dq[-1][0]:
                dq.pop()
            dq.append((cost,i))
            
        return dq[-1][0]