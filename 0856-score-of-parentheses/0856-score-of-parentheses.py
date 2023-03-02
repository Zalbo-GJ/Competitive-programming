class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        
        for i in s:
            
            
        
            if i == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack[-1] != "(":
                        score += 2*stack.pop()
                        
                    stack.pop()
                    stack.append(score)
            else:
                stack.append(i)

        return sum(stack)