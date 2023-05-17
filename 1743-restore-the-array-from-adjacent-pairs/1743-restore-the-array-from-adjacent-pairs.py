class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for u, v in adjacentPairs:
            graph[v].append(u)
            graph[u].append(v)
            indegree[v] += 1
            indegree[u] += 1
        
        start = -1
        for i in indegree.keys():
            if indegree[i] == 1:
                start = i
                break
                
        ans = []
        visited = set()
        que = deque([start])
        while que:
            
            node = que.popleft()
            
            ans.append(node)
            visited.add(node)
            for child in graph[node]:
                if child != node and child not in visited:
                    que.append(child)
    
        return ans
            
                
        