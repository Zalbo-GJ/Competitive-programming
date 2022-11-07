class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        
        time=0
        q = deque()
        
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)+1 #we add because its negative
                if cnt!=0:
                    q.append([cnt,time+n]) #current time and idle time
                    
            if( q and q[0][1] == time): 
                heapq.heappush(maxHeap, q.popleft()[0])
        return time