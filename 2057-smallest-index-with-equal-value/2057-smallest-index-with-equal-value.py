class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        for idx in range(len(nums)):
            if idx % 10 == nums[idx]:
                return idx
        return -1