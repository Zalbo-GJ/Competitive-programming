class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parents  = {i: i for i in range(len(accounts))}
        emails = {}
        
        def find( node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union( idx, email):
            urep = find(email)
            vrep = find(idx)
            
            parents[vrep] = urep
        
        for idx, val in enumerate(accounts):
            for email in val[1:]:
                if email in emails:
                    union(idx, emails[email])
                else:
                    emails[email] = idx
        
        temp = defaultdict(list)
        for key, val in emails.items():
            rep = find(val)
            temp[rep].append(key)
        
        ans = []
        for i in temp:
            user = accounts[i][0]
            acc = sorted(temp[i])
            
            ans.append([user , *acc ])
        
        return ans

        
       
                
            
            
            
            
            
            
            