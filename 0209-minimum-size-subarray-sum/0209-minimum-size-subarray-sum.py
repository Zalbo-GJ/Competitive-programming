class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        ans = len(nums)+1
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                ans = min(ans, r-l+1)
                summ -= nums[l]
                l += 1
        
        return ans if ans <= len(nums) else 0        