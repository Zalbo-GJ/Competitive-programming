class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
 
        max_sum = max(nums)
        running_sum = nums[0]
        start_idx = 0
        
        for idx in range(1,len(nums)):
            running_sum += nums[idx]
            if running_sum - nums[idx] < 0:
                running_sum = nums[idx]
                start_idx = idx 
            
            if running_sum > max_sum:
                max_sum = running_sum
        
        return max_sum
                
        