class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        
        for val in piles:
            heapq.heappush(heap, -val)
        
        while k:
            big = -heapq.heappop(heap)
            heapq.heappush(heap, -(big - floor(big / 2)))
            k -= 1
        print(heap)
        return -sum(heap)