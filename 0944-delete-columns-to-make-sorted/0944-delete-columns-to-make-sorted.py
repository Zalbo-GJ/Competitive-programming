class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        """
            step1: traverse through column not rows 
            step2: if the strs[row][n] < strs[row][n-1] increment deleted by 1 then break
            step3: return deleted
            
        """
        
        deleted = 0
        
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[row-1][col] > strs[row][col]:
                    deleted += 1
                    break
        
        return deleted