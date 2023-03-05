class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l = 0
        r = len(arr)-1
        
        while l <= r:
            
            mid = l + (r-l) // 2
            
            if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
                return mid
        
            elif arr[mid-1] < arr[mid]:
                l = mid 
            else:
                r = mid 
        
    