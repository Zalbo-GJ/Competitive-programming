class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        
        ans = 0
        p2 = 0
        
        for p1 in range(len(houses)):
            while p2 < len(heaters) - 1 and abs(houses[p1] - heaters[p2]) >= abs(houses[p1] - heaters[p2 + 1]):
                p2 += 1
            
            ans = max(ans, abs(houses[p1] - heaters[p2]))
        
        return ans
        