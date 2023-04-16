class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        temp = [0 for _ in range(n+5)]
        granted = 0
        maxReq = 0
        l = len(requests)
        
        def backtrack(ind):
            nonlocal temp, granted, maxReq
            if ind == l or granted + (l-ind) <= maxReq:
                if all(not temp[i] for i in range(n)):
                    maxReq = max(maxReq, granted)
                return
            
            fr, to = requests[ind]
            
            temp[fr] -= 1
            temp[to] += 1
            granted += 1
            
            backtrack(ind + 1)
            
            temp[fr] += 1
            temp[to] -= 1
            granted -= 1
            
            backtrack(ind + 1)
        
        backtrack(0)
        
        return maxReq
            