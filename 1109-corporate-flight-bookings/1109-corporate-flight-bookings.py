class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0]*(n+1)
        
        for first, last, seats in bookings:
            
            ans[first-1] += seats
            
            ans[last] -= seats
            
        for i in range(1,n):
            ans[i] += ans[i-1]
        return ans[:n]
        