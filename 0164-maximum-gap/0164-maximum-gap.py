class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for idx in range(1, len(nums)):
            ans = max(ans, abs(nums[idx] - nums[idx - 1]))
        
        return ans