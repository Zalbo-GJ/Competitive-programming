class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        ind = 0
        
        while ind + 1 < len(arr) and arr[ind] < arr[ind + 1]:
            ind += 1
        
        if ind == 0 or ind == len(arr)-1:
            return False
        
        while ind + 1 < len(arr) and arr[ind] > arr[ind + 1]:
            ind += 1
        
        
        return ind == len(arr) - 1
                    
        