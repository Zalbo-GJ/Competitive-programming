class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        for i in range(1, max(arr) + k + 10):
            if i not in arr:
                k -= 1
            
            if not k:
                return i
        