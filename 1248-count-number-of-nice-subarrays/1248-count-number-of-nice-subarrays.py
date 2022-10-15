class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        pre = ans = 0
        x = [0 if i%2==0 else 1 for i in nums]
        
        for i in x:
            pre += i
            
            if pre-k in d:
                ans += d[pre-k]
            if pre not in d:
                d[pre] = 1
            else:
                d[pre] += 1
        return ans