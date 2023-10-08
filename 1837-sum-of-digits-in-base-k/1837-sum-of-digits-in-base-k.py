class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = []
        if n == k and k == 10:
            return sum(list(map(int, str(n))))
        if n == k:
            return 1
        while n > 0:
            ans.append(n % k)
        
            n = (n // k)
        return sum(ans)