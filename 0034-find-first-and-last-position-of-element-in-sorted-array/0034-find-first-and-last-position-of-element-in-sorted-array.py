class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = [-1,-1]
        while l <= r:
            
            mid = (l + r)  // 2
            
            if nums[mid] >= target:
                
                if nums[mid] == target:
                    if mid - 1 == -1 or nums[mid-1] != target:
                        ans[0] = mid
                
                r -= 1
            else:
                l += 1
        
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            mid = (l + r)  // 2
            
            if  nums[mid] <= target:
                
                if nums[mid] == target:
                    if mid + 1 == len(nums) or nums[mid+1] != target:
                     

                        ans[1] = mid
                
                l += 1
            else:
                r -= 1
        
        return ans
        
            