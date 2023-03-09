class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        stack = []
        ans = [-1 for _ in range(size) ]
        
        for ind in range((2 * size),-1,-1):
           
            
            while stack and  nums[ind % size] >= stack[-1]:
                
                stack.pop()
            if stack:
                ans[ind % size] = stack[-1]
            stack.append(nums[ind%size])
            
            
        
        
        return ans
            