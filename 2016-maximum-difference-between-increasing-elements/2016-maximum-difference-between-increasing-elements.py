class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ans = max(ans, nums[j] - nums[i])
        
        return ans if ans else -1