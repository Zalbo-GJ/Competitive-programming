class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        r = k-1
        ans = len(blocks)
        while r < len(blocks):
            counts = 0
            
            for b in range(r-k+1,r+1):
                if blocks[b] == "W":
                    counts+=1
            ans = min(ans, counts)
            r+=1
            
        return ans
            