class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        que = deque(s)
        
        for _ in range(len(s)):
            if "".join(que) == goal:
                return True
            
            que.append(que.popleft())
        
        return False