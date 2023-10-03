class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        nums.sort(key = lambda x : x % 2)
        ans = []
        l = 0
        r = len(nums) - 1
        
        while l < r:
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r -= 1
        
        return ans