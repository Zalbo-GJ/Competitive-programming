class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prefix = [nums[0]]
        for i in range(1,len(nums)):
            left_prefix.append(nums[i] * left_prefix[i-1])
        
        right_prefix = [i for i in nums]
        for i in range(len(nums)-2,-1,-1):
            right_prefix[i] = nums[i] * right_prefix[i+1]
        
        for i in range(len(nums)):
            if i == 0:
                nums[i] = right_prefix[i+1]
            elif i == len(nums)-1:
                nums[i] = left_prefix[i-1]
            else:
                nums[i] = left_prefix[i-1] * right_prefix[i+1]
        
        return nums