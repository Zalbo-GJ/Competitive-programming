class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        _max = 0
        for num in nums:
            _max |= num
            
        n = len(nums)
        ans = 0
        def recur(ind, sub):
            nonlocal ans, _max
            if ind == n:
                if sub == _max:
                    ans += 1
                return
            
            recur(ind + 1, sub)
            recur(ind + 1, sub | nums[ind])
        
        recur(0, 0)
        
        return ans