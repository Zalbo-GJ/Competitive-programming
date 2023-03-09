class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.ans =[]
        self.curr = []
        
        
        self.combinations(1, n,k)
        
    
        return self.ans
    
    
    
    def  combinations(self, ind, n,k):
        
        if len(self.curr) == k:
            self.ans.append(self.curr.copy())
            return 
        
        if ind > n :
            return 
        
        
        
        self.curr.append(ind)
        
        self.combinations(ind + 1, n, k)
        
        self.curr.pop()
        
        self.combinations(ind +1 , n, k)
        
        return
        
        
        
            