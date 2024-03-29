class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        
        for non in range(len(nums)):
            
            if nums[non] != 0 and nums[zero] == 0:
                nums[non], nums[zero] = nums[zero], nums[non]
                
            if nums[zero] != 0:
                zero+=1