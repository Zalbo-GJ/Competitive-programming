class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = [[sum(mat[i]), i] for i in range(len(mat))]
        
        dic.sort()
        ans = []
        
        for idx in range(k):
            ans.append(dic[idx][1])
        
        return ans