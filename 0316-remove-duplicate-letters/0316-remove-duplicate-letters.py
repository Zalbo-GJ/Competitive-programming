class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        stack = []
        for ch in s:
            if ch in stack:
                count[ch] -= 1
                continue
                
            while stack and stack[-1]> ch and count[stack[-1]]>0:
                stack.pop()
            count[ch] -= 1

            stack.append(ch)
            
        return "".join(stack)
                
        
        