class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        arr = sorted(nums)
        
        ans = []
        
        for num in nums:
            ans.append(arr.index(num))
        
        return ans
        
        
        
        
        
                