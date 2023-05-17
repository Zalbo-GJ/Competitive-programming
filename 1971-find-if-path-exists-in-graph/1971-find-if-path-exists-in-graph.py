class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        rep = [i for i in range(n)]
        rank = [0 for i in range(n)]
        
        def find(node):
            
            while rep[node] != node:
                node = rep[node]
            return node
        def union(u, v):
            urep = find(u)
            vrep = find(v)
            urep, vrep = (urep, vrep) if rank[urep]>=rank[vrep] else (vrep, urep)

            rep[vrep] = urep
            rank[urep] += rank[vrep]
            
        for u, v in edges:
            union(u, v)
        
        return find(source)  == find(destination)