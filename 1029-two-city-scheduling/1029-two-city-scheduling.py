class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        temp = []
        for idx in range(len(costs)):
            temp.append([abs(costs[idx][0]- costs[idx][1]), idx])
        
        temp.sort(reverse = True)
        cityA = 0
        cityB = 0
        ans = 0
        for _, idx in temp:
            if cityA != len(costs)//2 and cityB != len(costs)//2:
                if costs[idx][0] < costs[idx][1]:
                    ans += costs[idx][0]
                    cityA += 1
                else:
                    ans += costs[idx][1]
                    cityB += 1
            else:
                if cityA != len(costs)//2:
                    ans += costs[idx][0]
                    cityA += 1
                else:
                    ans += costs[idx][1]
                    cityB += 1
        
        return ans
            