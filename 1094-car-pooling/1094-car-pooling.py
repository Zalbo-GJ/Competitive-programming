class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x: x[1])
        last_drop = max(i[2] for i in trips)

        arr = [0 for _ in range(last_drop + 5)]
        
        for passengers, pickup, dropoff in trips:
            
            arr[pickup] += passengers
            arr[dropoff] -= passengers
        
        running_sum = 0
        ans = 0
        
        for ind in range(last_drop+1):
            running_sum += arr[ind]
            
            ans = max(ans, running_sum)
        
        return ans <= capacity
        