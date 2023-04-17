class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        isPrime = [True for _ in range(right + 1)]
        isPrime[0] = isPrime[1] = False
        prev = 0
        bestdif = float('inf')
        best = 0
        i = 2
        while i <= right:
            
            if isPrime[i]:
                if left <= i <= right:
                    if prev:
                        diff = i - prev
                        if diff < bestdif:
                            bestdif = diff
                            best = prev
                    prev = i
                
                j = i * i
                while j <= right:
                    isPrime[j] = False
                    j += i
            i += 1
        
        if not best:
            return [-1,-1]
        
        return [best, best + bestdif]
        
        
        