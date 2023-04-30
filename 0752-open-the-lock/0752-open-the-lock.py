class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        visited = set(deadends)
        que = deque()
        que.append(['0000',0])
        
        def children(code):
            res = []
            for ind in range(4):
                digit = str((int(code[ind]) + 1) % 10)
                res.append(code[:ind] + digit + code[ind + 1:])
                digit = str((int(code[ind]) - 1 + 10) % 10)
                res.append(code[:ind] + digit + code[ind + 1:])
            
            return res
          
        while que:
            comb, turns = que.popleft()
            if comb == target:
                return turns
            
            for child in children(comb):
                if child not in visited:
                    visited.add(child)
                    que.append([child, turns + 1])
        
        return -1
                    
            
            
            
     