class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        weight = {(f, t): birr for f, t, birr in flights}
        short_path = [float('inf') for _ in range(n)]     
        heap = [(0, -1, src)]
        
        graph = defaultdict(list)
        for fro, to, w in flights:
            graph[fro].append(to)
        
        while heap:
            curr_dist, stops, curr_node = heapq.heappop(heap)
            
            if short_path[curr_node] <= stops:
                continue
            if stops > k:
                continue
            if curr_node == dst:
                return curr_dist
            
            short_path[curr_node] = stops
            
            for child in graph[curr_node]:
                dist = curr_dist + weight[curr_node, child]
                heapq.heappush(heap, [dist,stops + 1, child])

        return -1
            
                
                
            