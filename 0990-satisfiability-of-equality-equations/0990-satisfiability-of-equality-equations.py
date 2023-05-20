class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        rep = {i : i for i in string.ascii_lowercase}
        rank = {i: 1 for i in string.ascii_lowercase}
       

        def find( node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]

        def union( u, v):
            urep = find(u)
            vrep = find(v)

            urep, vrep =(vrep, urep) if rank[urep] <= rank[vrep] else (urep, vrep)

            rep[vrep] = urep
            rank[urep] += rank[vrep]
            
        

        for i in equations:
            eq = list(i)
            if eq[1] == "=":
                union( eq[0], eq[-1])

        for i in equations:
            eq = list(i)
            if eq[1] != "=":
                if find(eq[0]) == find( eq[-1]):
                    return False

        return True







