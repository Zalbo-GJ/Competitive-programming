class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 3:
            return 0
        isPrime = [1 for _ in range(n+1)]
        isPrime[0] = isPrime[1] = 0

        ind = 2
        
        while ind * ind <= n:
            
            if isPrime[ind]:
                
                j = ind * ind
                while j < n:
                    isPrime[j] = 0
                    j += ind
            ind += 1
        return  sum(isPrime)-1
        
       