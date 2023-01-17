class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        
        for j in range(len(matrix[0])):
            i = 0
            
            while i+1 < len(matrix) and j+1 < len(matrix[0]):
                
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                
                i += 1
                j += 1
            
            
        for i in range(1,len(matrix)):
            j = 0
            while i+1 < len(matrix) and j+1 < len(matrix[0]):
                
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                
                i += 1
                j += 1
        
        return True
            
            
        
                