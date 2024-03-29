class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        
        rep = {tuple(i) : tuple(i) for i in stones}
        rank =  {tuple(i) : tuple(i) for i in stones}
        
        def find(node):
            if rep[node] != node:
                rep[node] = find(rep[node])
            return rep[node]
        
        def union(x, y):
            
            xrep = find(x)
            yrep = find(y)
            
            if xrep!=yrep:
                rep[yrep] = xrep
        
        for i in range(len(stones)-1):
            for j in range(1,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1]==stones[j][1]:
                    union(tuple(stones[i]),tuple(stones[j]))
        
        mapp = defaultdict(int)
        
        for stone in stones:
            parent = find(tuple(stone))
            mapp[parent] += 1
        ans = 0
        for key in mapp:
            ans += mapp[key] -1
        return ans
        
                
        
        