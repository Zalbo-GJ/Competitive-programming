class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        ans = 0
        bridge = defaultdict(set)
        
        for city1, city2 in roads:
            bridge[city1].add(city2)
            bridge[city2].add(city1)
        
        for city1 in range(n):
            for city2 in range(city1 + 1, n):
                
                if city2 in bridge[city1]:
                    _max = len(bridge[city1]) + len(bridge[city2]) - 1
                else:
                    _max = len(bridge[city1]) + len(bridge[city2])
                
                ans = max(ans, _max)
        
        return ans
       