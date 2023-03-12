class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        temp = []
        
        def recur(ind):
            
            if ind >= len(nums):
                ans.append(temp.copy())
                return
    
            temp.append(nums[ind])
            recur(ind + 1)
            temp.pop()
            recur(ind + 1)
            
        recur(0)
        
        return ans
            
            
            
            