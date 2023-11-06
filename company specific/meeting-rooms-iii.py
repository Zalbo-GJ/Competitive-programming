class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        ans = [0 for _ in range(n)]
        rooms = list(range(n))
        taken = []
        heapq.heapify(rooms)

        for st, end in sorted(meetings):
            while taken and taken[0][0] <= st:
                heapq.heappush(rooms, heapq.heappop(taken)[1])
                
            if rooms:
                room = heapq.heappop(rooms)
                heapq.heappush(taken, [end, room])
            else:
                time, room = heapq.heappop(taken)
                heapq.heappush(taken, [time + end - st, room])
            
            ans[room] += 1 
            
        return ans.index(max(ans))