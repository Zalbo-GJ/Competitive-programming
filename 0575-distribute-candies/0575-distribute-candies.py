class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        count = Counter(candyType)
        if len(count) >= len(candyType) // 2:
            return len(candyType) // 2
        else:
            return len(count)