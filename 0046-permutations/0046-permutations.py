class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        curr = []
        ans = set()
        visited = set()
        
        def backtrack():
            
            if len(curr) == len(nums):
                if tuple(curr) not in ans:
                    ans.add(tuple(curr))
            
            
            for ind in range(len(nums)):
                
                if ind not in visited:
                    curr.append(nums[ind])
                    visited.add(ind)
                    backtrack()
    
                    visited.remove(ind)
                    curr.pop()
                    
        
        backtrack()
        
        return ans
                
