class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        best =tot= sum(cardPoints[:k])
        l,r = k-1,len(cardPoints)-1
        for i in range(k):
            tot+=(cardPoints[r]-cardPoints[l])
            r-=1
            l-=1
            best = max(best,tot)
        return best