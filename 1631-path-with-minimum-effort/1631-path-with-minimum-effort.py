class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        effort = [[float('inf') for _ in range(m)] for _ in range(n)]
        effort[0][0] = 0
        visited = set()
        heap = [(0, 0, 0)]
        
        while heap:
            eff, row, col = heapq.heappop(heap)
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for x, y in [[0,1],[1,0],[-1,0],[0,-1]]:
                newR, newC = row + x, col + y
                if newR < 0 or newC < 0 or newR >= n or newC >= m :
                    continue
                if eff == float('inf'):
                    diff =  abs(heights[row][col] - heights[newR][newC])
                else:
                    diff = max(eff, abs(heights[row][col] - heights[newR][newC]))
                
                if diff < effort[newR][newC]:
                    effort[newR][newC] = diff
                    heapq.heappush(heap, [diff, newR, newC])
        print(effort)     
        return effort[n - 1][m - 1]
                
                