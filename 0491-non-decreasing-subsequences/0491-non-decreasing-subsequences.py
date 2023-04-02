class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def recur(ind):
            
            if ind ==len(nums):
                if len(temp) > 1 and temp not in ans:
                    ans.append(temp.copy())   
                return 
            if not temp or nums[ind] >= temp[-1]:
                temp.append(nums[ind])
                recur(ind + 1)
                temp.pop()
                
            recur(ind + 1)
            
        recur(0)
        
        return ans
        