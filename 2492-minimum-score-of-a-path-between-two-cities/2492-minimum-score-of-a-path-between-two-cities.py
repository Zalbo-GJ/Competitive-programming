class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        def find(node):
            if rep[node] == node:
                return node
            
            res = find(rep[node])
            rep[node] = res
            return rep[node]
        
        ans = float('inf')
        rep = [i for i in range(n + 1)]
        rank = defaultdict(int)
       
        for i, j, d in roads:
            irep = find(i)    
            jrep = find(j)
           
            
            irep, jrep = (irep, jrep)  if rank[irep] >= rank[jrep] else (jrep, irep)
            
            rep[jrep] = irep
            rank[irep] += rank[jrep]
        
        roads.sort(key = lambda x: x[2])
         
        co = find(1)
        for i, j, d in roads:
            if find(i) == co:
                return d
        
        return ans
            
            
            
        
            
        
            
            