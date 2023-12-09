class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = []
        count = Counter(arr)
        
        for key, val in count.items():
            if val in unique:
                return False
            unique.append(val)
        
        return True
        