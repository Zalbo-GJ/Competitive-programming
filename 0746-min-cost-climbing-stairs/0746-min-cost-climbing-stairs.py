class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(ind):
            
            if ind >= len(cost):
                return 0 
            
            if ind not in memo:
                one = dp(ind + 1)
                two = dp(ind + 2)
                
                memo[ind] = min(one, two) + ( cost[ind] if ind != -1 else 0)
            
            return memo[ind]
        
        return dp(-1)