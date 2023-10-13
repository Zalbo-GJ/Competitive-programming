class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        nums = sorted(set(nums))
        ans = l
        start = 0
        
        for i in range(len(nums)):
            while start < len(nums) and nums[start] < nums[i] + l :
                start += 1
             
            ans = min(ans, l - ( start - i))

               
        return ans
                    
                