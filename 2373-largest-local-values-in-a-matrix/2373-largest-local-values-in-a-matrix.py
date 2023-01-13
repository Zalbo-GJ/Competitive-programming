class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
            1: iterate through the size of maxLocal
            2: for indx get max of the 3 rows including the one its on
            3: append max of the maxes 
        """
        ans = [[0]*(len(grid)-2)for _ in range(len(grid)-2)]
        
        for row in range(len(grid)-2):
            for col in range(len(grid)-2):
                
                
                row1 = max(grid[row][col:col+3])
                row2 = max(grid[row+1][col:col+3])
                row3 = max(grid[row+2][col:col+3])
                
                maxx = max(row1,row2,row3)
                ans[row][col] = maxx
            
        return ans
            