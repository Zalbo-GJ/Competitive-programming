class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ind = 0
        
        while ind < len(nums):
            
            if nums[nums[ind]-1] != nums[ind]:
                nums[nums[ind]-1], nums[ind] = nums[ind], nums[nums[ind]-1]
            else:
                ind += 1
        
        return nums[-1]
  