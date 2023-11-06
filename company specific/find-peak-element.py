class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        if len(nums) == 1:
            return 0
        mid = 0
        while mid < len(nums):
            
            if mid - 1 >= 0 and mid + 1 < len(nums):
                if nums[mid  + 1] < nums[mid] and nums[mid - 1] < nums[mid]: 
                    return mid
                elif nums[mid  + 1] < nums[mid]:
                    mid += 1
            
            elif mid - 1 < 0:
                if nums[mid  + 1] < nums[mid]:
                    return mid
            
            elif mid + 1 == len(nums):
                if nums[mid - 1] < nums[mid]:
                    return mid
                
            mid += 1
        
        return 0