class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        min_num = min(nums) + k
        max_num = max(nums) - k
        
        return max_num - min_num if min_num < max_num else 0
        