class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        ans = []
        
        for i in range(n):
            
            stack.append(i+1)
            ans.append("Push")
            if stack == target:
                return ans
            
            if stack[-1] != target[len(stack)-1]:
                stack.pop()
                ans.append("Pop")
                
            
       