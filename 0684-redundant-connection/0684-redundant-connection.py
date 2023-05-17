class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        rep = [i for i in range(len(edges) + 1)]
        
        def find(node):
            while rep[node] != node:
                node = rep[node]
            
            return node
        
        for u, v in edges:
            urep = find(u)
            vrep = find(v)
            
            if urep == vrep:
                return [u, v]
            
            urep, vrep =( vrep, urep )if urep >= vrep  else (urep, vrep)
            rep[vrep] = urep
            
        
            
            
            
            
            