class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        
        open_path = [[-1] * numCourses for _ in range(numCourses)]
        
        def bfs(start):
            que = deque([start])
            
            visited = set([start])
        
            while que:
                curr = que.popleft()
                
                open_path[start][curr] = True
                
                for child in graph[curr]:                                        
                    if child not in visited:
                        open_path[curr][child] = True
                        que.append(child)
                        visited.add(child)
                    
        
        answer = []
        for a, b in queries:
            if open_path[a][b] == -1:
                bfs(a)
                if open_path[a][b] == -1:
                    open_path[a][b] = False
            
            answer.append(open_path[a][b])
        
        return answer