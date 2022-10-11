class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        maxx =0
        for i in range(len(piles)/3,len(piles),2):
            maxx += piles[i]
        return maxx