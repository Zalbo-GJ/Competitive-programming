class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i,j in enumerate(sorted(citations)[::-1]):
            
            if i >= j:
                return i
        return len(citations)