class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack.append([char, stack[-1][1] + 1])
            else:
                stack.append([char, 1])
                
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        ans = []
        for pack in stack:
            ans.append(pack[0])
        
        return "".join(ans)