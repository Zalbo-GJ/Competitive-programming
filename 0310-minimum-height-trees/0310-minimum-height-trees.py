class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        if n < 3:
            return [i for i in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        que = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                que.append(i)
        
        while n > 2:
            numNodes = len(que)
            n -= numNodes
            
            for _ in range(numNodes):
                leaf = que.popleft()
                par = graph[leaf].pop()
                graph[par].remove(leaf)
                
                if len(graph[par]) == 1:
                    que.append(par)
        
        return list(que)
        