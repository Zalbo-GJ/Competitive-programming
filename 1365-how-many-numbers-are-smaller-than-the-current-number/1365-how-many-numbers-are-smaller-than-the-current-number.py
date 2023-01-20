class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans = []
        d = {}
        temp = sorted(nums)
        
        for i in nums:
            indx = temp.index(i)
            ans.append(indx)
        
        return ans