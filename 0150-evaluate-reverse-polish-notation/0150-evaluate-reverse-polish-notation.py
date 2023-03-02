class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in range(len(tokens)):
            
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
                
            elif tokens[i] == "-":
                stack.append(-stack.pop() + stack.pop())
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                dividend = float(stack.pop())
                stack.append(int(stack.pop()/ dividend))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]
            
                
        