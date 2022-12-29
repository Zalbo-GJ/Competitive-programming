class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}

        for item in cpdomains:
            count, domain = item.split(' ')
            if domain not in d:
                d[domain] = int(count)
            else:
                d[domain] += int(count)
            
          
            for i in range(len(domain)):
                
                if domain[i] == '.':
                    string = domain[i+1:]      
                    
                    if string not in d:
                        d[string] = int(count)
                    else:
                        d[string] += int(count)
        
        return [str(d[i])+" "+i for i in d]
                    

