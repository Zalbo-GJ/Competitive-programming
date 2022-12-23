class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        man_dist = float('inf')
        ans = -1
        for i, point in enumerate(points):
            
            if point[0] == x or point[1] == y:
                dist = ((abs(x - point[0])) + abs(y - point[1]))
                if dist < man_dist:
                    man_dist = dist
                    ans = i
        return ans

                

