class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        zCount = 0
        ans = []
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                zCount += 1
            else:
                if i+1 < len(nums) and nums[i] == nums[i+1]:
                    ans.append(2*nums[i])
                    nums[i+1] = 0
                else:
                    ans.append(nums[i])
        
        for _ in range(zCount):
            ans.append(0)
        
        return ans