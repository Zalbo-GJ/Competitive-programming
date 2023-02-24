class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        summ = 0
        
        for i in range(len(nums)):
            summ += nums[i]
            nums[i] = summ
        return nums
            