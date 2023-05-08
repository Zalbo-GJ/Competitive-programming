class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        colors = [0 for _ in range(len(graph))]
        def dfs(node, color):
            
            if color == 1:
                colors[node] = 3
                return False
            
            colors[node]  = 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 2:
                    continue
                
                if not dfs(neighbor, colors[neighbor]):
                    colors[node] = 3
                    return False
            
            colors[node] = 2
            return True
        
        ans = []
        for n in range(len(graph)):
            if colors[n] != 3:
                if dfs(n, 0):
                    ans.append(n)
        
        return ans