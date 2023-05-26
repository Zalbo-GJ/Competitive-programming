class Solution:
    def rob(self, nums: List[int]) -> int:
       
        memo = {}
        def dp(ind):
            if ind >= len(nums):
                return 0
            
            if ind not in memo:
                wit = dp(ind + 2) + nums[ind]
                without = dp(ind + 1)
                memo[ind] = max(wit, without)
            
            return memo[ind]
        
        return dp(0)