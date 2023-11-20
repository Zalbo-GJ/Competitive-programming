class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        non = 0
        
        for i in range(len(nums)):
            if nums[non] != nums[i]:
                non += 1
                nums[non] = nums[i]
                
            
        return non + 1
            