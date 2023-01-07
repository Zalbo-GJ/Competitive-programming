class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        
        col = [[0]* len(grid) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                col[i][j] = grid[j][i]
                
        column_count = Counter(map(tuple, col))
        
        for i in grid:
            ans += column_count[tuple(i)]
        
        return ans
            