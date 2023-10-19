class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for idx in range(len(values)):
            graph[equations[idx][0]].append((equations[idx][1], values[idx]))           
            graph[equations[idx][1]].append((equations[idx][0], 1 / values[idx]))
        
        print(graph)
        def bfs(a, b):
            
            que = deque([[a, 1]])
            visited = set([a])
            if a not in graph or b not in graph:
                return float(-1)
            while que:
                
                node, val = que.popleft()
                if node == b:
                    return val
                
                for child, new_val in graph[node]:
                    if child not in visited:                        
                        que.append([child, val * new_val])
                        visited.add(child)
            
            return float(-1)
        ans = []
        for a, b in queries:
            ans.append(bfs(a, b))
        
        return ans
        
        