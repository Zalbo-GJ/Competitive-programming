class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        left_ptr = 0
        right_ptr = n - 1
    
        minDif = float("inf")
        
        minDif = min(minDif, nums[right_ptr - 3] - nums[left_ptr])
        minDif = min(minDif, nums[right_ptr - 2] - nums[left_ptr + 1]) 
        minDif = min(minDif, nums[right_ptr - 1] - nums[left_ptr + 2])                
        minDif = min(minDif, nums[right_ptr] - nums[left_ptr + 3])
        
        
        return minDif