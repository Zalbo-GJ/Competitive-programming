class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        ans = [-1 for _ in range(n)]
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        alpha = [0 for _ in range(26)]
        
        def dfs(node, par):
            prevCount = alpha[ord(labels[node]) - 97]
            curr = 0
            
            for child in graph[node]:
                if child != par:
                    dfs(child, node)
            
            alpha[ord(labels[node]) - 97] += 1
            ans[node] = alpha[ord(labels[node]) - 97] - prevCount
        
        dfs(0, -1)
        
        return ans
                
