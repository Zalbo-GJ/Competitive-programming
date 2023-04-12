class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        for i in edges[0]:
            for j in edges[1]:
                if i == j:
                    return i
        