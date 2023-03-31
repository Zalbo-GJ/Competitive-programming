class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ind = 0
        ans = []
        
        while ind < len(nums):
            
            if nums[nums[ind]-1 ]!= nums[ind]:
                
                nums[nums[ind]-1], nums[ind] = nums[ind], nums[nums[ind]-1]
                
            else:
                
                ind += 1
        
        for i in range(len(nums)):
            if nums[i]-1 != i:
                ans.append(nums[i])
        
        return ans
                    