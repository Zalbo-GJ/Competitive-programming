class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ind = 0
        
        while ind < len(nums):
            
            if nums[ind]-1 != ind:
                if nums[ind] == nums[nums[ind]-1]:
                    return nums[ind]
                nums[nums[ind]-1], nums[ind] = nums[ind], nums[nums[ind]-1]
            else:
                ind += 1
        
        return nums[-1]
  