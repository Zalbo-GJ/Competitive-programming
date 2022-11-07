class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        st = [-i for i in stones]
        heapq.heapify(st)
        
        while len(st) > 1:
            x = heapq.heappop(st) 
            y = heapq.heappop(st) 
            
            if x==y:
                continue
            heapq.heappush(st, (x-y))
        if st:
            return heapq.heappop(st) * -1
        return 0