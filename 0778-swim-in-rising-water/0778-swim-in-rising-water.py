class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        time = [[float('inf') for _ in range(n)] for _ in range(n)]
        time[0][0] = grid[0][0]
        visited = set()
        heap = [(time[0][0], 0, 0)]
        
        while heap:
            distance_till, row, col = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for x, y in [[0,1],[1,0],[0,-1],[-1,0]]:
                newR, newC = row + x , col + y
                if newR < 0 or newC < 0 or newR >= n or newC >= n:
                    continue
                if distance_till >= grid[newR][newC]:
                    distance = distance_till
                else:
                    distance =  grid[newR][newC]
                
                if distance < time[newR][newC]:
                    time[newR][newC] = distance
                    heapq.heappush(heap, [time[newR][newC], newR, newC])
        return time[n - 1][n - 1]
        
        
        
                
            