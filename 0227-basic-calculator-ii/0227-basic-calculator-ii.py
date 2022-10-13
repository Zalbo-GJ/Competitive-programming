class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        op = '+'
        num = 0
        
        for cnt, i in enumerate(s):
            if i.isdigit():
                num = num*10 + int(i)
            if i in '+-/*' or cnt == len(s)-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                elif op == '/':
                    stack.append(int(stack.pop()/ float(num)))
                op = i
                num = 0
        return sum(stack)