class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(map(str,nums))
        
        for i in range(n):
            digits = [val for val in nums[i]]
            nums.append(''.join(digits[::-1]))
            
        nums = list(map(int,nums))
        count = Counter(nums)
        
        return len(count)
