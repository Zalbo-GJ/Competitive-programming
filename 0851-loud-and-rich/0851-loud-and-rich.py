class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        ans = [i for i in range(len(quiet))]
        indegree = defaultdict(int)
        
        graph = defaultdict(list)
        for sor, dest in richer:
            graph[sor].append(dest)
            indegree[dest] += 1
            
        
        def bfs(que):
            
            while que:
                
                par = que.popleft()
                for child in graph[par]:
                    indegree[child] -= 1
                    
                    if not indegree[child]:
                        que.append(child)
                        
                    if quiet[ans[par]] < quiet[ans[child]]:
                        ans[child] = ans[par]
                    
        que = deque()
        for i in range(len(quiet)):
            if indegree[i] == 0:
                que.append(i)
        
        bfs(que)
        
        return ans
            
            
          
        
        