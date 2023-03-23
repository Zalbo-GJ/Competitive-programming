class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        l = 0

        while l < len(nums):

            if nums[l] != l:
                
                ptr = nums[l]
                if nums[l] == len(nums):
                    l+=1
                    continue
                    
                nums[ptr], nums[l] = nums[l], nums[ptr]
            else:
                l += 1

        for ind in range(len(nums)):

            if ind != nums[ind]:
                return ind
        
        return len(nums)