class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        
        
        def bfs(que, ans):
            
            while que:
                node = que.popleft()
                
                for child in graph[node]:
                    
                    ans[child].add(node)
                    ans[child] = ans[child].union(ans[node])
                    
                    indegree[child] -= 1
                    
                    if indegree[child] == 0:
                        que.append(child)
                    
        
        
        ans = [set() for _ in range(n)]
        graph = defaultdict(list)
        indegree = [0 for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v]  += 1
        que = deque()
        for i in range(n):
            if not indegree[i]:
                que.append(i)
        
        bfs(que, ans)
        ans = list(ans)
        for i in range(n):
            ans[i] = sorted(ans[i])
        
        return ans
        
            