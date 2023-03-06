class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        l = 1
        r = max(nums)
        mini = r
        while l <= r:
            
            mid = (l + r) // 2
            
            if self.divisor(nums,mid) <= threshold:
                r = mid - 1
                mini = min(mid, mini)
            else:
                l = mid  + 1
        
        return mini
    
    
    def divisor(self, nums,div):
        summ = 0
        for num in nums:
            
            summ += ceil(num/div)
        
        return summ