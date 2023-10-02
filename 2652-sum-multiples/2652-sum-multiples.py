class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for num in range(1, n + 1):
            if not num % 3 or not num % 5 or not num % 7:
                ans += num
        
        return ans