class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck).values()
        
        return reduce(gcd,count) >= 2