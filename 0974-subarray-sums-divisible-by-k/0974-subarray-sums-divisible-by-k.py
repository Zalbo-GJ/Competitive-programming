class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        presum = ans = 0
        dic = {0:1}
        for i in range(len(nums)):
            presum += nums[i]
            
            if presum % k in dic:
                ans += dic[presum % k]
            
            if presum % k in dic:
                dic[presum % k] += 1
            else:
                dic[presum % k] = 1
        
        return ans