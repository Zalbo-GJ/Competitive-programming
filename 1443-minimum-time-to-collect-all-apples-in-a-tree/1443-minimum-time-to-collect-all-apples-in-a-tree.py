class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        for p,c in edges:
            graph[p].append(c)
            graph[c].append(p)

        def dfs(cur, par):
            time = 0
            for child in graph[cur]:
                if child == par:
                    continue
                downtime = dfs(child,cur)
                
                if downtime or hasApple[child]:
                    time += 2 + downtime
            
            return time

        return dfs(0, -1)
        