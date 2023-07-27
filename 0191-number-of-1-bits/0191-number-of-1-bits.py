class Solution:
    def hammingWeight(self, n: int) -> int:
        
        arr = list(map(int, str(bin(n))[2:]))
        return sum(arr)
        