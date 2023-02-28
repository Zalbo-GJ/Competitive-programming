class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        self.swaper(0,len(s)-1,s)
        
            
            
    def swaper(self,l,r,s):
        
        
        if  l < r:
            
            s[l], s[r] = s[r], s[l]
            
            self.swaper(l+1,r-1,s)
        
            
        