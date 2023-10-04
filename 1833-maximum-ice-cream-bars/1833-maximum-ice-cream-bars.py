class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins < costs[0]:
            return 0
        for idx in range(len(costs)):
            
            if not coins or coins < costs[idx]:
                return idx
            coins -= costs[idx]
        
        return len(costs)