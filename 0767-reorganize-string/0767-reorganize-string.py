class Solution:
    def reorganizeString(self, s: str) -> str:
        count = [[0, i] for i in range(27) ]
        for i in s:
            count[ord(i)- ord('a')][0] -= 1
            
        heapq.heapify(count)
        strin = ['Z']
        while heapq.nsmallest(1, count)[0][0] != 0:
            p = heapq.heappop(count)
            if (ord(strin[-1]) - ord('a')) == p[1]:
                sec = heapq.heappop(count)
                strin.append(chr(sec[1]+ 97))
                heapq.heappush(count ,[sec[0]+1, sec[1]] ) 
            strin.append(chr(p[1]+97))
            heapq.heappush(count, [p[0]+1, p[1]] )  
                
        
        return "".join(strin[1:]) if len(s) == len(strin) - 1 else ""