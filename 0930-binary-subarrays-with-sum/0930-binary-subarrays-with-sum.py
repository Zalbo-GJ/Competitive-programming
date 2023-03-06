class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        dic = {0:1}
        presum = 0
        ans = 0
        for num in nums:
            
            presum += num
            
            if presum - goal in dic:
                ans += dic[presum - goal]
            
            if presum in dic:
                dic[presum] += 1
            else:
                dic[presum] = 1
        
        return ans
            
            
        
        