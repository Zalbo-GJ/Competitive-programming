class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        ans = float('inf')
        weight = {(i[0], i[1]): i[2] for i in times}
        time = [float('inf') for _ in range(n + 1)]
        time[0] = 0
        time[k] = 0
        heap = [(0, k)]
        graph = defaultdict(list)
        visited = set()

        for fro, to, w in times:
            graph[fro].append(to)
        
        while heap:
            curr_distance, curr_node = heappop(heap)
            
            if curr_node in visited:
                continue
            visited.add(curr_node)
            
            for child in graph[curr_node]:
                distance = curr_distance + weight[(curr_node, child)]
                
                if distance < time[child]:
                    time[child] = distance
                    heapq.heappush(heap, [distance, child])
        
        return max(time) if max(time) != float('inf') else -1
                
            
            
            