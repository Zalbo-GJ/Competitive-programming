class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for i in s:
            que = []
            if i == ')':
                while stack[-1] != "(":
                    que.append(stack.pop())
                stack.pop()
                while que != []:
                    stack.append(que.pop(0))
            else:
                stack.append(i)
        return ''.join(stack)