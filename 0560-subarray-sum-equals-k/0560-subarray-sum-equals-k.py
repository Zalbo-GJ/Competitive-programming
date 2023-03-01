class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        presum = 0
        dic = {0:1}
        ans = 0
        for i in nums:
            presum += i
            
            if presum - k in dic:
                ans += dic[presum-k]
                
            
            if presum in dic:
                dic[presum] += 1
            else:
                dic[presum] = 1
                    
        return ans