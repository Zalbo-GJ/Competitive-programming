class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        rep = {i : i for i in string.ascii_lowercase}
        
        
        def find(node):
            if rep[node] == node:
                return node
            
            rep[node] = find(rep[node])
            return rep[node]
        
        def union(x, y):
            
            xrep = find(x)
            yrep = find(y)
            
            xrep, yrep = (yrep, xrep) if xrep >= yrep else (xrep, yrep)
            
            rep[yrep] = xrep
        
        
        for i in range(len(s1)):
            
            union(s1[i], s2[i])
        ans = []
        for i in baseStr:
            ans.append(find(i))
        
        return "".join(ans)
            
        
        
            
            
            
            
        