class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                op += nums[idx - 1] - nums[idx] + 1
                nums[idx] = nums[idx - 1] + 1
        
        return op