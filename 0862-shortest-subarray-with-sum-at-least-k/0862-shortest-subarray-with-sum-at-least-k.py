class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pre_sum = [0]
        mono_q = deque()
        for i in range(n):
            pre_sum.append(nums[i]+ pre_sum[-1])
        ans = n+1
        for idx , s in enumerate(pre_sum):
            while mono_q and s-pre_sum[mono_q[0]] >=k:
                
                
                ans = min(ans,idx -mono_q.popleft() )
            while mono_q and s <= pre_sum[mono_q[-1]]:
                mono_q.pop()
                
            mono_q.append(idx)
        return ans if ans < n+1 else -1