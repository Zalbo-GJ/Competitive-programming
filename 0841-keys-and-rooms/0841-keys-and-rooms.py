class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        opened = [False]* len(rooms)
        opened[0] = True
        visited = {0}
        que = deque([0])
      
        
        while que:
            
            ind = que.popleft()
            
            
            for nd in rooms[ind]:
                
                if nd not in visited:
                    opened[nd] = True
                    visited.add(nd)
                    que.append(nd)
        
        
        return True if len(rooms) == sum(opened) else False
            
        