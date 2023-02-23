class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ans = avr = sum(nums[:k])
        
        for r in range(k, len(nums)):
            
            avr += nums[r]-nums[r-k]
            
            ans = max(ans, avr)
            
            
        return ans/float(k)
                
            
            
        
        