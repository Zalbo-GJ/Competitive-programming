class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for idx in range(len(edges)):
            graph[edges[idx][0]].append([ edges[idx][1], succProb[idx] ])
            graph[edges[idx][1]].append([ edges[idx][0], succProb[idx] ])
    
        max_prob = [0.0 for _ in range(n)]
        max_prob[start_node] = 1.0
        
        heap = [(-1, start_node)]
        
        while heap:
            prob, node = heapq.heappop(heap)
            
            if node == end_node:
                return -prob
            
            for child, child_prob in graph[node]:
                dist = -prob * child_prob
                if dist > max_prob[child]:
                    heapq.heappush(heap, [-dist, child])
                    max_prob[child] = dist
                    
        return 0                
            
        
        
        
            