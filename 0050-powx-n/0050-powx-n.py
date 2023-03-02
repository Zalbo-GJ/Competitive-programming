class Solution:
    def myPow(self, x: float, n: int) -> float:
        
       
        return self.poww(x,n) if n >= 0 else 1/self.poww(x,-n)
    
    
    def poww(self,x,n):
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            return self.poww(x*x, n/2)
        else:
            return x * self.poww(x*x, (n-1)/2)
        