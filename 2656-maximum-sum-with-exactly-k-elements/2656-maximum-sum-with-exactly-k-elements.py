class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        p = 0
        ans = 0
        
        nums.sort()
        
        for _ in range(k):
            ans += nums[-1]  + p
            p += 1
        
        return ans