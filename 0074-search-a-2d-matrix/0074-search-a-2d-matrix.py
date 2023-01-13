class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            1: for every row check if last element of row is > target
            2: for that row iterate through to check if it exists
            3: if exist return True else False
        """
        
        for row in matrix:
            
            if row[-1] >= target:
                for item in row:
                    if item == target:
                        return True
                
                return False