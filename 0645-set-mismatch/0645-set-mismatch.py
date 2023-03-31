class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        ind = 0
        ans = []
        while ind < len(nums):
            
            if nums[ind] != nums[nums[ind]-1]:
                nums[nums[ind]-1], nums[ind] = nums[ind], nums[nums[ind]-1]
            else:
                ind += 1
        
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return [nums[i], i+1]