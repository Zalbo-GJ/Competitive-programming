class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        return max(count, key = count.get)