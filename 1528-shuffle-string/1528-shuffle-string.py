class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        d = sorted(zip(indices, s))
        
        shuffle = [i[1] for i in d]
        
        return "".join(shuffle)
        
        