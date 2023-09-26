class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        ans = 0
        while r < len(nums):
            if nums[r] == 0:
                r += 1
                l = r
            else: r += 1
            
            ans = max(ans, r - l)
        
        return ans
            
        