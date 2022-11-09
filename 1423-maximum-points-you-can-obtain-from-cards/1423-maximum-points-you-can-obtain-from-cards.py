class Solution:
    def maxScore(self, cardPoints, k):       
        max_sum = 0     
        for i in range(k):
            max_sum += cardPoints[i]
        ans = max_sum
        l= k-1
        r = len(cardPoints)-1
        while r >= len(cardPoints) - k:
            max_sum += cardPoints[r] - cardPoints[l]
            ans = max(max_sum,ans)
            r-=1
            l-=1
            
        return ans
        
