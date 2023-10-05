class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        dig_sum = 0
        for i in nums:
            dig_sum += sum(list(map(int, str(i))))
        
        return abs(sum(nums) - dig_sum )