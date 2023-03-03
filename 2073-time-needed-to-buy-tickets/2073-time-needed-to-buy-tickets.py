class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        que = Deque(tickets)
        count = 0
        while que:
            front = que.popleft()
            k -= 1
            count +=1
            
            if front - 1 != 0:

                que.append(front - 1)
            else:

                if k == -1:
                    break
            
            
                
            if k == -1:
                k = len(que)-1
          
        return count
                
            
            
                
        
        