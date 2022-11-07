class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0]*(n+1)
        
        for i in range(n-1,-1,-1):
            point , brain = questions[i]
            
            dp[i] = max(dp[i+1], point+ dp[min(n,i+brain+1)])
        return dp[0]