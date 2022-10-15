class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        last_d = 0
        for i in trips:
            last_d = max(last_d,i[2])
            
        ans = [0]* (last_d+1)
        
        for pas, start, end in trips:
            ans[start] += pas
            ans[end] -= pas
        if ans[0] > capacity:return False
        for i in range(1,len(ans)):
            ans[i] += ans[i-1]
            if ans[i]> capacity:
                return False
        
        return True