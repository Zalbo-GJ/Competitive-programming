class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(1,len(matrix[i])):
                
                self.matrix[i][j] += matrix[i][j-1]
        
        for j in range(len(matrix[0])):
            for i in range(1,len(matrix)):
                
                self.matrix[i][j] += matrix[i-1][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        
        ans = self.matrix[row2][col2]
        
        if col1-1 >= 0:
            ans -= self.matrix[row2][col1-1]
        if row1-1 >= 0:
            ans -= self.matrix[row1-1][col2]
        if row1-1 >=0 and col1-1 >= 0:
            ans += self.matrix[row1-1][col1-1]
        return ans
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)