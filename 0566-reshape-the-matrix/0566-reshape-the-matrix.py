class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        """
            step1: iterate through the mat list  with two ptrs
            step2: for number of column append to a temp list
            step3: append the temp list to the ans
        """
        ans = []
        temp = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                temp.append(mat[row][col])
                if len(temp) == c:
                    ans.append(temp)
                    temp = []
                
        return ans if len(ans) == r else mat
                
                
                