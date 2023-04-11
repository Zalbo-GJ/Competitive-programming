class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        temp = []
        def dfs(ind):
            
            temp.append(ind)
            if ind == len(graph)-1:
                ans.append(temp.copy())
                temp.pop()
                return 
            
                
            for val in graph[ind]:
                dfs(val)
                
            temp.pop()
        
        dfs(0)
        
        return ans