class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [(scores[idx], ages[idx]) for idx in range(len(ages))]
        pairs.sort()
        
        dp = sorted(scores)
        for idx in range(1, len(ages)):
            score, age = pairs[idx]
            for j in range(idx - 1, -1, -1):
                sec_score, sec_age = pairs[j]

                if sec_age <= age :
                    dp[idx] = max(dp[idx], score + dp[j])
        
        return max(dp)
                    
                
                
                