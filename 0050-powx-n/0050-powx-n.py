class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return float(x**n)
        def poww(x,n):
            
            if n ==0:
                return 1
            elif n%2==0:
                return poww(x*x, n/2)
            else:
                return x* poww(x*x,(n-1)/2)

        
        return poww(x,n) if n>=0 else 1/poww(x,-n)