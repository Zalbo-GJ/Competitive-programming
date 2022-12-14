class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        r,c = len(matrix),len(matrix[0])
        for i in range(r):
            #Horizontal prefix
            for j in range(1,c):
                matrix[i][j]+= matrix[i][j-1]
        #Vertical pefix after the horizontal is done
        for i in range(c):
            for row in range(1,r):
                matrix[row][i] += matrix[row-1][i]
                
        self.m = matrix     
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = self.m[row2][col2]
        
        if col1-1 >= 0:
            ans -= self.m[row2][col1-1]
        if row1-1 >= 0:
            ans -= self.m[row1-1][col2]
        if row1-1 >=0 and col1-1 >= 0:
            ans += self.m[row1-1][col1-1]
        return ans
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)