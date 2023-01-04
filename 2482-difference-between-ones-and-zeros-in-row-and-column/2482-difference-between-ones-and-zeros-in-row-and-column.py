class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        row_sum = []
        
        for i in range(len(grid)):
            zero_cnt = 0
            one_cnt = 0
            for j in range(len(grid[0])):
                
                if grid[i][j] == 0:
                    zero_cnt += 1
                else:
                    one_cnt +=1
            
            row_sum.append([zero_cnt, one_cnt])
      
        
        col_sum = []
        
        for j in range(len(grid[0])):
            zero_cnt = 0
            one_cnt = 0
            
            for i in range(len(grid)):
                
                if grid[i][j] == 0:
                    zero_cnt += 1
                else:
                    one_cnt +=1
            
            col_sum.append([zero_cnt, one_cnt])
      
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                grid[i][j]  =  row_sum[i][1] + col_sum[j][1] - row_sum[i][0] - col_sum[j][0]
            
        return grid
                    
            
          
        
        
        
            
        