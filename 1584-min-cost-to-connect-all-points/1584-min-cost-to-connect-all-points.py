class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]

        def union(u,v):
            parent[u] = v
                
        parent = [i for i in range(len(points))]
        mand = []
        visited = set()
        
        for i in range(len(points)):
            for j in range(len(points)):
                
                if i != j and (j, i) not in visited:
                    dist = (abs(points[i][0]- points[j][0])) + (abs(points[i][1] - points[j][1]))
                    mand.append([dist, i, j])
                    visited.add((i,j))
        
        mand.sort()
        ans = 0
        for cost, i, j in mand:
            ipar = find(i) 
            jpar = find(j)
            
            if ipar != jpar:
                union(ipar, jpar)
                ans += cost
        
        return ans
        
        