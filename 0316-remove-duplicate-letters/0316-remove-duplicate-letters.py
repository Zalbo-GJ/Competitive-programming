class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        count = Counter(s)
        
        for ind in range(len(s)):
            
            count[s[ind]] -= 1
            if s[ind] in stack:
                continue
            
            while stack and  s[ind] <= stack[-1]:

                if count[stack[-1]] >= 1:
                  
                    stack.pop()
                else:
                    break
           
                                    
            stack.append(s[ind])
        
        
        return "".join(stack)
        