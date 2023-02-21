class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        """
        1.take max element until i then flip it the flip [:i+1]
        
        """
        
        i = len(arr)-1
        ans = []
        while i >= 0:
            maxInd = arr[:i+1].index(max(arr[:i+1]))
            
            if maxInd == i:
                pass
            else:
                arr[:maxInd+1] = arr[:maxInd+1][::-1]
                ans.append(maxInd+1)
                
                arr[:i+1] = arr[:i+1][::-1]
                ans.append(i+1)
            i -= 1
        
  
        return ans
            
            
                