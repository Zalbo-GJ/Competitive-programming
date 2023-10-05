class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in nums:
            digs = list(map(int, str(i)))
            ans.extend(digs)
        
        return ans