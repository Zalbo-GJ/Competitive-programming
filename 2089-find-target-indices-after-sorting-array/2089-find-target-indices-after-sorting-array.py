class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        ans = []
        for i,j in enumerate(nums):
            
            if j == target:
                ans.append(i)
        return ans