class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        full_sum = sum(nums)
        if not full_sum % 2:
            half = full_sum // 2
        else:
            return False
        
        memo = {}
        def dp(left_sum, idx):
            if idx == len(nums):
                return False

            if left_sum == half:
                return True
            
            if (left_sum, idx) not in memo:

                memo[(left_sum, idx)] = dp(left_sum + nums[idx], idx + 1) or dp(left_sum, idx + 1)

            return memo[(left_sum, idx)]
        
        return dp(0, 0)