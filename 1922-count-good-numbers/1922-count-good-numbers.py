class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10 ** 9 + 7
        even = pow(5 ,n // 2, m)        
        prime = pow(4 ,n // 2, m)
        if not n % 2:
            return ((even % m) * (prime % m)) % m
        else:
            return ((even % m) * (prime % m) * 5) % m