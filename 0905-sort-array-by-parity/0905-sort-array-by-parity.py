class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for odd in range(len(nums)):
            
            for even in range(odd,len(nums)):
                
                if nums[odd]%2 !=0 and nums[even]%2 == 0:
                    nums[odd],nums[even] = nums[even],nums[odd]
        return nums
        
        