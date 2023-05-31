class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(ind, summ):
            
            if ind >= len(nums):
                if summ == target:
                    return 1
                return 0
            
            if (ind, summ) not in memo:
                sub = dp(ind + 1, summ - nums[ind])
                add = dp(ind + 1, summ + nums[ind])
                memo[(ind, summ)] = sub + add
            
            return memo[(ind, summ)]
        
        return dp(0,0)
            
            
            
                    