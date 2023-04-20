class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        ans = []
        child = set() 
        for ed in edges:
            child.add(ed[1])
        
        for ind in range(n):
            if ind not in child:
                ans.append(ind)
        
        return ans