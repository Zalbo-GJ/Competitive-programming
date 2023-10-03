class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        def bfs(que):
            print(que)
            while que:
                node = que.pop()
                for child in graph[node]:
                    que.append(child)

            return node 
                    
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a, b in paths:
            graph[a].append(b)
            indegree[b] += 1
        
        que = []
        for a, b in paths:
            if indegree[a] == 0:
                que.append(a)
        
        return bfs(que)