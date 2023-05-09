class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def bfs(que):
            order = []
            while que:
                
                node = que.popleft()
                order.append(node)
                for child in graph[node]:
                    indegree[child] -= 1
                    if not indegree[child]:
                        que.append(child)
                        
            if len(order) != numCourses:
                return False
            
            return True
        
        graph = defaultdict(list)
        indegree = defaultdict()
        for to, first in prerequisites:
            graph[first].append(to)
            if to in indegree:
                indegree[to] += 1
            else:
                indegree[to] = 1
                
       
        que = deque()
        for i in range(numCourses):
            if i not in indegree or not indegree[i]:
                que.append(i)
        
        return bfs(que)
        
                