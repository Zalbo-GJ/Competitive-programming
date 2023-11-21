class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brace = { '{':'}', '(':')' , '[':']' }
        stack = []
        
        for i in s:
            if i in brace:
                stack.append(i)
            elif stack == [] or brace[stack.pop()] != i:
                return False
        return stack == []
                
            
        