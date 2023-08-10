class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        count = Counter(nums)
        
        return True if sum(count.values()) > len(count.keys()) else False