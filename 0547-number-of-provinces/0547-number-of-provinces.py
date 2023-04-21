class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(ind):
            if tuple(isConnected[ind]) in visited:
                return
            
            visited.add(tuple(isConnected[ind]))
            for j in range(n):
                if j != ind and isConnected[ind][j] == 1:
                    dfs(j)
        
            
        ans = 0
        visited = set()
        n = len(isConnected)
        for i in range(n):
            if tuple(isConnected[i]) not in visited:
                dfs(i)
                ans += 1
        
        return ans