class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = [[1]*len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if matrix[i][j] == 0:
                    
                    for row in range(len(matrix)):
                        mat[row][j] = 0
                    for col in range(len(matrix[0])):
                        mat[i][col] = 0
        
          
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               
                if mat[i][j] == 0:
                
                    matrix[i][j] = mat[i][j]
               