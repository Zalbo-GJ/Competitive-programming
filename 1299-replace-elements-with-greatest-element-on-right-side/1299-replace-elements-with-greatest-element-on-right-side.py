class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        indx = 0
        for i in range(len(arr)):
            
            if i == indx:
                maxx = -1
                for j in range(i+1,len(arr)):
                    
                    if arr[j] > maxx:
                        maxx = arr[j] 
                        indx = j
                
            arr[i] = maxx
        
        return arr
        