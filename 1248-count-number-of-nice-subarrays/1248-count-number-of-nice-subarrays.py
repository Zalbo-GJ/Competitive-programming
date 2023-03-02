class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        nums = [0 if i % 2 == 0 else 1 for i in nums]
        
        presum = ans = 0
        dic = {0:1}
        for i in range(len(nums)):
            presum += nums[i]
            
            if presum-k in dic:
                ans += dic[presum-k]
            
            if presum in dic:
                dic[presum] += 1
            else:
                dic[presum] = 1
        
        return ans