class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = []
        for i in matrix:
            for j in i:
                heapq.heappush(q,j)
       
        while k>1:
            heapq.heappop(q)
            k-=1
        return heapq.heappop(q)