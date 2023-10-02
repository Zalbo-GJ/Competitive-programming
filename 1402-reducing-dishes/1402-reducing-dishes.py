class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(time, idx):
            if idx >= len(satisfaction):
                return  0
                 
            return max( (( time * satisfaction[idx])) + dp(time + 1, idx + 1,), dp(time, idx + 1))
        
        return  dp(1,0)
        