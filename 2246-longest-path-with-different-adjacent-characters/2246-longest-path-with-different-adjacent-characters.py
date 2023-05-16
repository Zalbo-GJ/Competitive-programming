class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        n = len(s)
        for i in range(1, n):
            graph[parent[i]].append(i)
        
        def dfs(node):
            nonlocal ans
            
            long, sec = 0, 0
            for child in graph[node]:
                long_from_child = dfs(child)
                               
                if s[child] == s[node]:
                    continue

                if long_from_child > long:
                    sec = long
                    long = long_from_child
                elif long_from_child > sec:
                    sec = long_from_child

            ans = max(ans, long + sec + 1)
                     
            return long + 1 
        
        ans = 1
        dfs(0)
        
        return ans                        
        
                               
            
            
        