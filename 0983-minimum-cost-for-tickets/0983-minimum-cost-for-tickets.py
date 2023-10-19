class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(idx):
            
            if idx >= len(days):
                return 0
            
            one_day = costs[0] + dp(idx + 1)
            
            day7 = days[idx] + 7
            seven_idx = len(days)
            for i in range(idx, len(days)):
                if days[i] >= day7:
                    seven_idx = i
                    break
                    
            week = costs[1] + dp(seven_idx)
            
            day30 = days[idx] + 30
            month_idx = len(days)
            for i in range(idx, len(days)):
                if days[i] >= day30:
                    month_idx = i
                    break
                    
            month = costs[2] + dp(month_idx)

            return min(one_day, week, month)
        
        return dp(0)