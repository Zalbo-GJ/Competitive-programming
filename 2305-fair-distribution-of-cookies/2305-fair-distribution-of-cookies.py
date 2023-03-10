class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        children= [0 for _ in range(k)]
        fair = float('inf')
        
        def recur(ind):
            nonlocal children, fair
            if ind >= len(cookies):
                fair = min(fair, max(children))
                return
            
            if fair <= max(children):
                return
        
            for j in range(k):
                children[j] += cookies[ind]
                recur(ind + 1)
                children[j] -= cookies[ind]
                
        recur(0)
        
        return fair
             
                

