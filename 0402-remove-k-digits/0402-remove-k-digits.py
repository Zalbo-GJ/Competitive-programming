class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for i in num:
            while k and stack and i < stack[-1]:
                stack.pop()
                k-=1
            stack.append(i)
        ans = ''.join(stack[:len(stack)-k])
        return str(int(ans)) if ans else "0"