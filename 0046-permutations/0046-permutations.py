class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        curr = []
        ans = set()
        
        
        def backtrack(visited):
            
            if len(curr) == len(nums):
                if tuple(curr) not in ans:
                    ans.add(tuple(curr))
        
            
            for ind in range(len(nums)):
                if not (visited & (1 << ind)):
                    
                    curr.append(nums[ind])
                    backtrack( visited | (1 << ind) )
                    curr.pop()
        
        backtrack(0)
        
        return ans
                
