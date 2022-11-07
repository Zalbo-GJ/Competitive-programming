class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        jumps = []
        
        for i in range(len(heights)-1):
            jump = heights[i+1]-heights[i]
            
            if heights[i] >= heights[i+1]:
                continue;
            if heights[i] < heights[i+1]:
                heapq.heappush(jumps, jump)
            if len(jumps) > ladders:
                bricks -= heapq.heappop(jumps)
                if bricks < 0:
                    return i
        return len(heights)-1
                