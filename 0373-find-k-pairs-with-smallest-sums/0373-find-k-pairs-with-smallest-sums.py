class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        heapq.heappush(heap, [nums1[0] + nums2[0], 0 ,0])
        visited = set()
        ans = []
        lenU = len(nums1)
        lenV = len(nums2)
        while heap and k :
            
            _, u, v = heapq.heappop(heap)
            ans.append([nums1[u], nums2[v]])
            
            if u + 1 < lenU and (u + 1 , v) not in visited:
                heapq.heappush(heap,[nums1[u + 1] + nums2[v], u + 1 ,v])
                visited.add((u + 1, v))
            
            if v + 1 < lenV and (u, v + 1 ) not in visited:
                heapq.heappush(heap,[nums1[u] + nums2[v + 1], u ,v + 1])
                visited.add((u, v + 1))
            
            k -= 1
        
        return ans
            
        
        