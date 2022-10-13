class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = left = 0
        bottom, right = len(matrix),len(matrix[0])
        ans = []
        
        while left<right and top < bottom:
            
            #Top-left to right
            for i in range(left,right):
                ans.append(matrix[top][i])
            top+=1
            #Top-right to bottom
            for i in range(top,bottom):
                ans.append(matrix[i][right-1])
            right-=1
            if not(left < right and top < bottom):
                break
            #Bottom-right to left
            for i in range(right-1,left-1,-1):
                ans.append(matrix[bottom-1][i])
            bottom-=1
            #Bottom-left to top
            for i in range(bottom-1,top-1,-1):
                ans.append(matrix[i][left])
            left+=1
            
            
        return ans