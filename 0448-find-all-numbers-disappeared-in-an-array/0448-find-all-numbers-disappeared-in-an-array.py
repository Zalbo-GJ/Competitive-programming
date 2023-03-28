class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ans = []
        for ind in range(len(nums)):
            nums[abs(nums[ind])-1] = -(abs(nums[abs(nums[ind])-1]))
        
        for ind in range(len(nums)):
            if nums[ind] > 0:
                ans.append(ind + 1)
                
        return ans