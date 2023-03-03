class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        r = x
        
        while l<=r:
            mid = l+(r-l) //2

            
            if mid*mid < x:
                l  = mid+1
                
            elif mid*mid > x:
                r = mid-1
                dum = mid -1
                
                if dum*dum < x:
                    return dum
            else:
                return mid
        