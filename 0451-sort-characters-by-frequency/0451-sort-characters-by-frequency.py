class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        s = list(s)
        s.sort(key = lambda x: (count[x], x), reverse = True)
        
        return "".join(s)